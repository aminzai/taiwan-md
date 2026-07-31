export const meta = {
  name: 'babel-vi-haiku-batch',
  description:
    'Translate vi-missing articles with Haiku, escalate failures to Sonnet',
  phases: [
    { title: 'Haiku', detail: '每篇一隻 Haiku agent 翻譯 + 自驗' },
    { title: 'Sonnet 升級', detail: 'Haiku 沒過的改派 Sonnet 重做' },
    { title: '驗收', detail: '獨立跑 verify-agent-batch 並跟 agent 自述對帳' },
  ],
};

const RESULT = {
  type: 'object',
  properties: {
    target: { type: 'string' },
    passed: { type: 'boolean' },
    failed_checks: { type: 'array', items: { type: 'string' } },
    rounds: { type: 'number' },
    notes: { type: 'string' },
  },
  required: ['target', 'passed'],
};

function rules(t, extra) {
  return `你是 Taiwan.md 的翻譯 worker。把一篇中文文章完整翻成越南文並落檔。

**前景串行執行。禁止用 run_in_background 後結束回合等通知——你的環境裡背景指令完成不會通知你自己，那等於停擺。**

## 任務
- 來源：\`knowledge/${t.zh}\`（完整讀）
- 落檔路徑：\`knowledge/${t.target}\`（**路徑不可自創，就是這個**）

## 步驟
1. 完整讀 \`docs/editorial/per-language/TRANSLATION-vi.md\`（越南文規範：主權詞彙、人名、標點）
2. 完整讀來源文章
3. 翻譯後用 Write 落檔

## Frontmatter 硬規則
- **原樣照抄不翻**：\`author\` \`date\` \`featured\` \`readingTime\` \`lastVerified\` \`lastHumanReview\` \`category\` \`image\` \`imageCredit\` \`difficulty\`
- **要翻**：\`title\` \`description\` \`imageAlt\` \`tags\` \`subcategory\`
- **必須新增，值精確照抄**：
\`\`\`
translatedFrom: '${t.zh}'
sourceCommitSha: '${t.sha}'
sourceContentHash: '${t.chash}'
sourceBodyHash: '${t.bhash}'
\`\`\`
- \`translatedAt\` 用當下 ISO8601 UTC

## 內容硬規則（違反就被閘門擋下）
- **腳註定義數必須與原文完全相同**，\`[^n]:\` 每條都要在
- **所有網址原樣保留**，一個字元都不能改（不補斜線、不 percent-encode）
- **\`## \` 章節數與原文相同**
- **不可殘留中文**（越南文非漢字語言，正文連續漢字＝洩漏）。專有名詞用越南文慣例或漢越音，必要時括號附原文
- **\`[[wikilink]]\` 保持原文中文目標不變**（例：\`[[張雨生]]\` 就寫 \`[[張雨生]]\`）。**絕對不要把方括號拆掉變純文字**——那會讓站內連結消失，而且三個檢查都抓不到
- 台灣＝台灣，不可寫成中國的一部分；不要套用中國官方用語
${extra}
## 自驗（必跑）
\`\`\`
python3 scripts/tools/lang-sync/verify-translation.py "${t.zh}" knowledge/${t.target}
python3 scripts/tools/lang-sync/cjk-leak-check.py knowledge/${t.target}
python3 scripts/tools/article-health.py knowledge/${t.target} --profile=pre-commit
\`\`\`
三個都要沒有 hard fail。不通過就修到通過。

**不要 git add、不要 commit。**

回傳 JSON：target（落檔路徑）、passed（三檢查是否都無 hard fail）、failed_checks（若有，列出哪幾項）、rounds（修幾輪）、notes（一句話，特別是你猶豫或取捨的地方）。`;
}

// args 可能以 JSON 字串抵達（Workflow 工具已知陷阱），防禦性解析
const tasks = typeof args === 'string' ? JSON.parse(args) : args;

phase('Haiku');
log(`批次 ${tasks.length} 篇：Haiku 第一輪，失敗自動升 Sonnet`);

const results = await pipeline(
  tasks,
  (t) =>
    agent(rules(t, ''), {
      model: 'haiku',
      label: `haiku:${t.target.split('/').pop()}`,
      phase: 'Haiku',
      schema: RESULT,
    }).then((r) => ({ task: t, first: r, tier: 'haiku' })),
  async (r) => {
    if (r.first && r.first.passed) return r;
    const why = r.first
      ? (r.first.failed_checks || []).join(', ')
      : 'agent 無回傳';
    const esc = await agent(
      rules(
        r.task,
        `
## 這篇 Haiku 已經失敗過
上一輪沒過的項目：${why}
請重做整篇（不要在壞檔上修補），特別注意上述項目。
`,
      ),
      {
        model: 'sonnet',
        label: `sonnet:${r.task.target.split('/').pop()}`,
        phase: 'Sonnet 升級',
        schema: RESULT,
      },
    );
    return { ...r, escalated: esc, tier: 'sonnet' };
  },
);

const ok = results.filter(Boolean);
const haikuPass = ok.filter((r) => r.tier === 'haiku').length;
const sonnetTried = ok.filter((r) => r.tier === 'sonnet');
const sonnetPass = sonnetTried.filter(
  (r) => r.escalated && r.escalated.passed,
).length;

log(
  `Haiku 過 ${haikuPass}/${tasks.length}；升 Sonnet ${sonnetTried.length} 篇，其中過 ${sonnetPass}`,
);

// ── 獨立驗收（結構性強制，不是靠自律）─────────────────────────────
// 2026-07-31 教訓：agent 自述 48 過、主 session 實測 47（REFLEXES #31），
// 而且當時的複驗是現寫的三閘門迴圈，比 verify-batch 弱——10 條站內死鏈
// 因此 commit 出去。把驗收接進工作流本身，批次就**不可能**在沒驗過的
// 狀態下結束；寫在文件上的「記得驗」只是自律，這一段才是閘門。
phase('驗收');
const claims = ok.map((r) => ({
  target: r.task.target,
  passed: r.tier === 'haiku' ? true : !!(r.escalated && r.escalated.passed),
}));
const audit = await agent(
  `跑 Taiwan.md 的批次翻譯驗收，如實回報，不要修任何檔案。

1. 把下面兩份 JSON 各自寫成檔案（用 Write 工具寫到 /tmp/）：

tasks.json：
${JSON.stringify(tasks.map((t) => ({ zh: t.zh, target: t.target })))}

claims.json：
${JSON.stringify(claims)}

2. 執行：
\`\`\`
cd /Users/cheyuwu/Projects/taiwan-md
python3 scripts/tools/lang-sync/verify-agent-batch.py --tasks /tmp/tasks.json --lang vi --claims /tmp/claims.json
\`\`\`

3. 把輸出裡的三段如實抓出來回傳：逐檔硬閘門的通過/未過數與未過清單、
   與 agent 自述對帳的結果（宣稱過但實際沒過的清單）、以及 verify-batch
   的 Errors/Warnings 數字。

**不要修檔案、不要 git add、不要 commit。** 你的工作只有驗收與如實回報——
如果數字難看就照實報，這一步存在的意義就是抓出 agent 自述與實際的落差。`,
  {
    model: 'sonnet',
    label: 'audit:batch',
    phase: '驗收',
    schema: {
      type: 'object',
      properties: {
        actual_pass: { type: 'number' },
        actual_fail: { type: 'number' },
        failed_targets: { type: 'array', items: { type: 'string' } },
        overclaimed: { type: 'array', items: { type: 'string' } },
        verify_batch_errors: { type: 'number' },
        summary: { type: 'string' },
      },
      required: ['actual_pass', 'actual_fail'],
    },
  },
);
if (audit) {
  log(
    `獨立驗收：實際過 ${audit.actual_pass} / 未過 ${audit.actual_fail}` +
      (audit.overclaimed && audit.overclaimed.length
        ? `；⚠️ agent 宣稱過但實際沒過 ${audit.overclaimed.length} 篇`
        : '；自述與實測一致'),
  );
}

return {
  audit,
  total: tasks.length,
  haiku_pass: haikuPass,
  escalated: sonnetTried.length,
  sonnet_pass: sonnetPass,
  details: ok.map((r) => ({
    zh: r.task.zh,
    target: r.task.target,
    tier: r.tier,
    passed: r.tier === 'haiku' ? true : !!(r.escalated && r.escalated.passed),
    failed_checks:
      r.tier === 'haiku'
        ? []
        : (r.escalated && r.escalated.failed_checks) || [],
    notes:
      (r.escalated && r.escalated.notes) || (r.first && r.first.notes) || '',
  })),
};
