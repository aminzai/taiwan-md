import { icons } from '../../src/icons/taiwan-icons.mjs';
import { STAGES } from './prompts.mjs';
const esc = (value) =>
  String(value ?? '').replace(
    /[&<>"']/g,
    (char) =>
      ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[
        char
      ],
  );
const glyph = (name) =>
  `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="${icons[name]}"/></svg>`;
export function renderRun(state) {
  return `<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Rewrite Guide · ${esc(state.id)}</title><style>
:root{color-scheme:light;--ink:#233f3b;--paper:#f5f1e8;--line:#c7c9b8;--accent:#9c4f35}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.75 system-ui,sans-serif}main{max-width:1100px;margin:auto;padding:40px 24px}header{border-bottom:1px solid var(--ink);padding-bottom:28px}small,.eyebrow{letter-spacing:.15em;font-size:12px}h1{font:clamp(34px,6vw,68px)/1.2 Georgia,serif;margin:12px 0}h2{font-size:24px}.status{color:var(--accent)}nav{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:32px 0}nav a{border:1px solid var(--line);padding:18px;color:inherit;text-decoration:none}nav a[aria-current=step]{border:2px solid var(--accent)}section{margin:32px 0}details{border-top:1px solid var(--line);padding:15px 0}summary{cursor:pointer;font-weight:600}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#ebe8de;padding:16px;font-size:13px}p{max-width:75ch}li{margin:12px 0}code{overflow-wrap:anywhere}.warning{border-left:3px solid var(--accent);padding-left:18px}@media(max-width:600px){nav{grid-template-columns:1fr 1fr}main{padding:25px 16px}}</style><main><header><div class="eyebrow">TAIWAN.MD / EDITORIAL FIELD NOTES</div><h1>讓文章，值得被讀。</h1><p>Rewrite Guide · ${esc(state.scope === 'section' ? '局部試寫' : '文章工作')}</p><p class="status">${esc(state.status)} · 第 ${esc(state.attempt)} 輪</p><small>唯讀匯出快照 · 不代表已發布 · ${esc(state.id)}</small></header>
${state.stale.length ? `<p class="warning">工作檔已改變，舊裁決失效：${esc(state.stale.map((item) => item.path).join('、'))}</p>` : ''}
<nav aria-label="工作階段">${STAGES.map((stage, index) => `<a href="#${stage.id}" ${state.stage === stage.id ? 'aria-current="step"' : ''}>${glyph(['question', 'antenna', 'code', 'brain', 'balance', 'door'][index])}<br><small>0${index + 1} / ${state.accepted[stage.id] ? '已接受' : state.stage === stage.id ? '目前' : '待完成'}</small><br>${esc(stage.title)}</a>`).join('')}</nav>
${STAGES.map(
  (stage) =>
    `<section id="${stage.id}"><h2>${esc(stage.title)}</h2><p>${esc(stage.prompt)}</p>${
      state.submissions
        .filter((s) => s.stage === stage.id)
        .map(
          (submission) =>
            `<details><summary>第 ${esc(submission.attempt)} 輪 · ${esc(submission.actor)} · ${esc(submission.review?.verdict ?? '等待審閱')}</summary><pre>${esc(JSON.stringify(submission.data, null, 2))}</pre>${submission.review ? `<p><b>${esc(submission.review.actor)}</b>：${esc(submission.review.rationale)}</p><pre>${esc(JSON.stringify(submission.review.evidence, null, 2))}</pre>` : ''}${submission.artifacts.map((a) => `<details><summary>${esc(a.path)} · ${esc(a.sha256.slice(0, 12))}</summary><pre>${esc(a.text)}</pre></details>`).join('')}</details>`,
        )
        .join('') || '<p>尚無提交。完整性與編輯品質分開驗證。</p>'
    }</section>`,
).join('')}
<section><h2>每一次改變，都有原因</h2><ol>${state.events.map((event) => `<li><small>${esc(event.at)}</small><br>${esc(event.type)} · ${esc(event.stage)}${event.reason ? `<p>${esc(event.reason)}</p>` : ''}</li>`).join('')}</ol></section><footer>此工作台是執行紀錄，AI 評閱仍需校準。使用 next / submit / review / backtrack 更新原始 run，再重新匯出。</footer></main></html>`;
}
