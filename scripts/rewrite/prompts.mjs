/** The executable mission registry: no duplicated stage rules in the CLI. */
export const STAGES = [
  {
    id: 'orient',
    title: '找到讀者真正的問題',
    role: 'editor',
    fields: [
      'readerQuestion',
      'subjectExplanation',
      'candidateAngles',
      'uncertainties',
    ],
    prompt:
      '先用朋友聽得懂的話說明主題本身。讀者為什麼打開？提出至少兩個可被材料推翻的角度，不急著宣判核心矛盾。列出未知；不要把缺少搜尋結果當成現實缺席。',
  },
  {
    id: 'investigate',
    title: '讓材料改變你的想法',
    role: 'researcher',
    fields: ['claims', 'counterEvidence', 'searchLimits', 'changedMind'],
    prompt:
      '每個承重主張附來源 URL、原始段落位置、查閱日期、支持到哪裡與不支持什麼。分開事實、推論和查無。搜尋數不是品質證明；哪份反證改變了原先角度？必要時退回 orient。',
  },
  {
    id: 'compose',
    title: '把人與事件帶到讀者面前',
    role: 'writer',
    fields: ['draftPath', 'editorialChoices', 'unresolved'],
    prompt:
      '寫完整且能讀的稿；局部試寫只完成指定範圍。讓動作、場景、轉折和有意義的材料推動理解，勿虛構紀實場景。可以改順序；發現論點錯了就 backtrack。刪減理由留在工作紀錄，不灌進正文替自己辯護。',
  },
  {
    id: 'cold-read',
    title: '把稿交給沒看過藍圖的人',
    role: 'reader',
    fields: [
      'contextDisclosure',
      'retelling',
      'changedUnderstanding',
      'confusions',
      'repetitions',
      'forcedConclusions',
    ],
    prompt:
      '只讀這份稿，不看研究與作者藍圖。用自己的話說這是什麼、發生了什麼；指出哪個細節改變你的理解、哪裡困惑或重複、哪裡被強推結論。不是檢查作者是否完成自己的計畫。若已看過藍圖，明說不是獨立盲讀並換讀者。',
  },
  {
    id: 'verify',
    title: '對回原文，也檢查圖表',
    role: 'verifier',
    fields: ['sourceChecks', 'mechanicalChecks', 'unresolved'],
    prompt:
      '對回每個承重主張、直接引語與腳註描述的原始來源。數字分開核對對象、時間、單位、分母；圖表不能把不同公司或換股前後價格當投資報酬。查無不推出不存在。先判矛盾成立，再判哪邊錯。機械檢查要有實際命令、退出碼與輸出工件；不把機械 PASS 當事實確認。',
  },
  {
    id: 'release',
    title: '決定這份稿值不值得交出去',
    role: 'chief-editor',
    fields: ['recommendation', 'remainingLimits', 'humanReview'],
    prompt:
      '用具體段落解釋這份稿值得推薦的理由，確認未解問題與人類實際審閱狀態。品質未達就回退，不能以關卡全部通過為理由。此關只完成交付準備，不代表已發布；局部試寫只交付試稿。',
  },
];
export const stageById = (id) => STAGES.find((stage) => stage.id === id);

// Structural contracts only; no field is a semantic quality score.
export const FIELD_TYPES = {
  candidateAngles: 'angles',
  claims: 'claims',
  mechanicalChecks: 'checks',
  uncertainties: 'notes',
  counterEvidence: 'notes',
  searchLimits: 'notes',
  unresolved: 'notes',
  confusions: 'notes',
  repetitions: 'notes',
  forcedConclusions: 'notes',
  sourceChecks: 'notes',
  remainingLimits: 'notes',
};
export const fieldTemplate = (field) =>
  FIELD_TYPES[field] === 'angles'
    ? ['', '']
    : FIELD_TYPES[field] === 'claims'
      ? [{ source: '', location: '', support: '', doesNotSupport: '' }]
      : FIELD_TYPES[field] === 'checks'
        ? [{ command: '', exitCode: null, output: '' }]
        : FIELD_TYPES[field] === 'notes'
          ? []
          : '';
export function fieldValid(field, value) {
  const text = (v) => typeof v === 'string' && v.trim().length > 0;
  switch (FIELD_TYPES[field]) {
    case 'angles':
      return Array.isArray(value) && value.length >= 2 && value.every(text);
    case 'notes':
      return text(value) || (Array.isArray(value) && value.every(text));
    case 'claims':
      return (
        Array.isArray(value) &&
        value.length > 0 &&
        value.every(
          (v) =>
            v &&
            ['source', 'location', 'support', 'doesNotSupport'].every((k) =>
              text(v[k]),
            ),
        )
      );
    case 'checks':
      return (
        Array.isArray(value) &&
        value.length > 0 &&
        value.every(
          (v) =>
            v &&
            text(v.command) &&
            text(v.output) &&
            (v.exitCode === null || Number.isInteger(v.exitCode)),
        )
      );
    default:
      return text(value);
  }
}
