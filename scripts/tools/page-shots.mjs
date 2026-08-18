#!/usr/bin/env node
/**
 * page-shots.mjs — 站上頁面截圖儀器（Playwright，repo 內已裝）。
 *
 * 兩種模式：
 *   square   孢子配圖：把指定元素裁成正方形（預設 1280×1280 實體像素），隱藏浮動 chrome、
 *            等 justfont 載入、必要時自動 zoom 讓元素塞進正方形；每張寫 alt 進 README。
 *   sections 驗收截圖：整頁＋每個 section 各一張（desktop／mobile／dark／任意語言），給人眼逐張看。
 *
 * 誕生：2026-08-18 /budget 孢子配圖與 v2 驗收。之前每次都現寫一支 .mjs 用完刪，
 * 哲宇 directive「把這次使用來截圖的儀器留起來納入自己的系統」→ 落成 canonical 工具。
 *
 * 用法：
 *   node scripts/tools/page-shots.mjs square --url https://taiwan.md/budget/ \
 *        --spec data/budget/spore-shots.json --out public/spore-images --prefix budget-decade
 *   node scripts/tools/page-shots.mjs sections --url http://localhost:4330/budget \
 *        --out /tmp/shots --widths 1280,390 --dark --sections "#s0,#s1,#s2"
 *
 * spec（square 模式）JSON：
 *   { "hide": ["#header-container", ...]（可選，覆蓋預設）,
 *     "shots": [ { "n": 1, "target": "#s0",             ← 單一或多個 selector（union bbox）
 *                  "targets": ["#c-fn-share", "#c-fn-growth"],
 *                  "viewport": 640, "dpr": 2,          ← 640×640 CSS px @2 = 1280 實體像素（預設）
 *                  "margin": 16,                       ← 元素外留白（CSS px）
 *                  "hideExtra": [".bp-lede"],          ← 這一張額外隱藏
 *                  "alt": "一句 alt 給發文用" } ] }
 *
 * 幾何：只截目標元素（union bbox＋margin），比正方形小就白底補到正方形，比正方形大就等比縮小——
 * 不會把鄰居截進來。字要清楚：實體字高低於 22px 會在 stdout 警告（縮小 viewport 讓版面重排、或拆兩張）。不改 src/。
 */
import { chromium } from 'playwright';
import sharp from 'sharp';
import { mkdirSync, readFileSync, writeFileSync, existsSync } from 'node:fs';
import { resolve, join } from 'node:path';

const args = process.argv.slice(2);
const mode = args[0];
const opt = (k, d) => {
  const i = args.indexOf(`--${k}`);
  return i >= 0 ? args[i + 1] : d;
};
const flag = (k) => args.includes(`--${k}`);
if (!['square', 'sections'].includes(mode)) {
  console.error('usage: page-shots.mjs <square|sections> --url <url> [--spec f] [--out dir] [--prefix p] [--widths 1280,390] [--dark] [--sections sel,sel]');
  process.exit(2);
}
const url = opt('url');
if (!url) { console.error('--url required'); process.exit(2); }
const out = resolve(opt('out', 'public/spore-images'));
mkdirSync(out, { recursive: true });

// 預設隱藏：站上的浮動 chrome（header／語言 banner／回饋鈕／reader-settings／.md 鈕／skip link／dev toolbar）
const DEFAULT_HIDE = [
  '#header-container', '#main-header', '.skip-link', '#md-btn', '.floating-md', '#back-to-top',
  '#reader-settings-toggle', '.reader-settings-panel', '.twmd-fb-fab', 'astro-dev-toolbar', '.bg-tip',
];

async function prepPage(page, hide, dark) {
  await page.goto(url, { waitUntil: 'networkidle', timeout: 90000 });
  if (dark) await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
  // 等 justfont（正式站才會 active；本機／headless 多半 inactive）
  let jf = false;
  for (let i = 0; i < 6; i++) {
    jf = await page.evaluate(() => document.documentElement.classList.contains('jf-active'));
    if (jf) break;
    await page.waitForTimeout(1000);
  }
  await page.waitForTimeout(800);
  await page.addStyleTag({ content: `${hide.join(',')} { display:none !important }` });
  return jf;
}

async function unionBox(page, sels) {
  return page.evaluate((sels) => {
    const els = sels.flatMap((s) => Array.from(document.querySelectorAll(s)));
    if (!els.length) return null;
    els[0].scrollIntoView({ block: 'start' });
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (const el of els) {
      const r = el.getBoundingClientRect();
      x0 = Math.min(x0, r.left + window.scrollX); y0 = Math.min(y0, r.top + window.scrollY);
      x1 = Math.max(x1, r.right + window.scrollX); y1 = Math.max(y1, r.bottom + window.scrollY);
    }
    return { x: x0, y: y0, w: x1 - x0, h: y1 - y0 };
  }, sels);
}

async function minFontPx(page, sels) {
  return page.evaluate((sels) => {
    const els = sels.flatMap((s) => Array.from(document.querySelectorAll(s + ' *')));
    let m = Infinity;
    for (const el of els) {
      if (!el.textContent?.trim()) continue;
      const fs = parseFloat(getComputedStyle(el).fontSize);
      if (fs && el.getClientRects().length) m = Math.min(m, fs);
    }
    return m === Infinity ? null : m;
  }, sels);
}

const browser = await chromium.launch();
try {
  if (mode === 'square') {
    const specPath = opt('spec');
    if (!specPath) { console.error('--spec required for square'); process.exit(2); }
    const spec = JSON.parse(readFileSync(resolve(specPath), 'utf8'));
    const prefix = opt('prefix', 'shot');
    const hide = spec.hide || DEFAULT_HIDE;
    const readme = [`# ${prefix} — 孢子配圖（page-shots.mjs square）`, '', `來源：${url}`, `產生：${new Date().toISOString().slice(0, 10)}`, ''];
    for (const s of spec.shots) {
      const vp = s.viewport || 640;
      const dpr = s.dpr || Math.round((1280 / vp) * 1000) / 1000;
      const ctx = await browser.newContext({ viewport: { width: vp, height: vp }, deviceScaleFactor: dpr, colorScheme: 'light' });
      const page = await ctx.newPage();
      const jf = await prepPage(page, [...hide, ...(s.hideExtra || [])], false);
      const sels = s.targets || [s.target];
      // 先把 viewport 拉到整頁高再量 bbox：fullPage 截圖會臨時改 viewport 高度、sticky／details 版面會位移，
      // 量測與截圖必須在同一個幾何下（2026-08-18 三種「拖了幾天」卡被切掉一行的教訓）
      const docH = await page.evaluate(() => document.documentElement.scrollHeight);
      await page.setViewportSize({ width: vp, height: Math.min(docH, 16000) });
      await page.waitForTimeout(500);
      const box = await unionBox(page, sels);
      if (!box) { console.error(`✗ #${s.n} 找不到 ${sels.join(', ')}`); await ctx.close(); continue; }
      // 只截目標元素：比正方形大就 sharp 等比縮小、比正方形小就白底補到正方形（不把鄰居截進來）
      const margin = s.margin ?? 16;
      const clip = { x: Math.max(0, box.x - margin), y: Math.max(0, box.y - margin), width: box.w + margin * 2, height: box.h + margin * 2 };
      const file = join(out, `${prefix}-${String(s.n).padStart(2, '0')}.png`);
      const raw = join(out, `.${prefix}-${String(s.n).padStart(2, '0')}.raw.png`);
      await page.screenshot({ path: raw, clip });
      const side = s.side || 1280;
      const meta = await sharp(raw).metadata();
      const scale = Math.min(1, side / Math.max(meta.width, meta.height));
      await sharp(raw)
        .resize({ width: Math.round(meta.width * scale), height: Math.round(meta.height * scale), fit: 'inside' })
        .extend({
          top: Math.floor((side - Math.round(meta.height * scale)) / 2), bottom: Math.ceil((side - Math.round(meta.height * scale)) / 2),
          left: Math.floor((side - Math.round(meta.width * scale)) / 2), right: Math.ceil((side - Math.round(meta.width * scale)) / 2),
          background: '#ffffff',
        })
        .png()
        .toFile(file);
      const { unlinkSync } = await import('node:fs');
      unlinkSync(raw);
      const mf = await minFontPx(page, sels);
      const phys = mf ? +(mf * dpr * scale).toFixed(1) : null;
      const zoom = +(dpr * scale).toFixed(3);
      const warn = phys !== null && phys < 22 ? ' ⚠️ 實體字高 < 22px（縮小 viewport 或拆兩張）' : '';
      console.log(`✓ #${s.n} ${file}  vp ${vp}@${dpr} 縮放 ${zoom} jf=${jf} minFont≈${phys}px${warn}`);
      readme.push(`## ${String(s.n).padStart(2, '0')}\n- 目標：\`${sels.join(', ')}\`\n- 設定：viewport ${vp} @${dpr}，實體縮放 ${zoom}${s.hideExtra ? `，額外隱藏 ${s.hideExtra.join(', ')}` : ''}；白底補正方形；justfont ${jf ? 'active' : 'inactive'}；最小字高≈${phys}px${warn}\n- alt：${s.alt || ''}\n`);
      await ctx.close();
    }
    writeFileSync(join(out, `${prefix}-README.md`), readme.join('\n'));
    console.log(`README → ${join(out, `${prefix}-README.md`)}`);
  } else {
    const widths = (opt('widths', '1280,390')).split(',').map(Number);
    const secs = (opt('sections', 'section')).split(',');
    const dark = flag('dark');
    for (const w of widths) {
      const ctx = await browser.newContext({ viewport: { width: w, height: 900 }, deviceScaleFactor: 1, colorScheme: dark ? 'dark' : 'light' });
      const page = await ctx.newPage();
      const errs = [];
      page.on('pageerror', (e) => errs.push(e.message));
      const jf = await prepPage(page, [], dark);
      const tag = `${w}${dark ? '-dark' : ''}`;
      await page.screenshot({ path: join(out, `full-${tag}.png`), fullPage: true });
      for (const sel of secs) {
        const els = await page.$$(sel);
        for (let i = 0; i < els.length; i++) {
          const id = (await els[i].getAttribute('id')) || `${sel.replace(/[^a-z0-9]/gi, '')}${i}`;
          await els[i].screenshot({ path: join(out, `${id}-${tag}.png`) });
        }
      }
      console.log(`✓ ${tag} → ${out}  jf=${jf} pageerrors=${errs.length}`);
      await ctx.close();
    }
  }
} finally {
  await browser.close();
}
