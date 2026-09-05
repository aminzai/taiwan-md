#!/usr/bin/env node
/**
 * toc-anchor-audit.mjs
 * ────────────────────
 * 走訪 dist 底下每個 index.html，對每個含 `id="toc"` 的頁面，把 TOC 連結的
 * `data-toc-id="…"`（等同 `href="#…"`）對照該頁所有 `<h2 id="…">` /
 * `<h3 id="…">` 的集合，找出「TOC 連結指到一個頁面上實際不存在的
 * heading id」的頁面。
 *
 * 背景：TableOfContents.astro 的 extractHeadings() 曾有一個永遠抓不到既有
 * id 的 regex bug（見該檔內詳細註解），導致部分頁面的 TOC 連結 id 跟
 * article-render.ts renderer.heading 實際寫在 <h2>/<h3> 上的 id 不一致。
 * 本腳本用來量化「修之前」「修之後」dist 裡這個問題的頁數與比例。
 *
 * Usage:
 *   node scripts/tools/toc-anchor-audit.mjs [--json] [--dist <path>]
 *
 * Output（human）：
 *   - 有 TOC 的頁數
 *   - 至少一條 TOC 連結不符的頁數與比例
 *   - 前 10 個不符樣本（頁面路徑 + toc id + 最接近的實際 heading id）
 *
 * Output（--json）：
 *   { totalTocPages, mismatchPages, mismatchRatio, samples: [...] }
 */

import { readFileSync, readdirSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '../..');

// 純 node:fs 遞迴走訪，避免為了一支審計腳本新增 fast-glob 依賴
// （repo 目前完全沒有這個套件，連間接依賴都沒有）。
function walk(dir, out = []) {
  let entries;
  try {
    entries = readdirSync(dir, { withFileTypes: true });
  } catch {
    return out;
  }
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(full, out);
    } else if (entry.isFile() && entry.name === 'index.html') {
      out.push(full);
    }
  }
  return out;
}

function parseArgs(argv) {
  const args = { json: false, dist: path.join(repoRoot, 'dist') };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--json') args.json = true;
    else if (a === '--dist') args.dist = path.resolve(argv[++i]);
  }
  return args;
}

// 極簡 Levenshtein，只用來在報告裡挑「最接近的實際 heading id」給人類看，
// 不參與符合/不符合的判定（判定永遠是精確字串比對，見下方 mismatchIds 計算）。
function levenshtein(a, b) {
  const m = a.length;
  const n = b.length;
  const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
  for (let i = 0; i <= m; i++) dp[i][0] = i;
  for (let j = 0; j <= n; j++) dp[0][j] = j;
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      dp[i][j] =
        a[i - 1] === b[j - 1]
          ? dp[i - 1][j - 1]
          : 1 + Math.min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]);
    }
  }
  return dp[m][n];
}

function closestId(target, candidates) {
  if (candidates.length === 0) return null;
  let best = candidates[0];
  let bestDist = levenshtein(target, best);
  for (const c of candidates.slice(1)) {
    const d = levenshtein(target, c);
    if (d < bestDist) {
      bestDist = d;
      best = c;
    }
  }
  return best;
}

function auditFile(filePath, distRoot) {
  const html = readFileSync(filePath, 'utf8');
  if (!html.includes('id="toc"')) return null;

  // Scope to the <nav id="toc">...</nav> block so we don't accidentally
  // pick up data-toc-id-looking strings elsewhere on the page.
  const navMatch = html.match(/<nav\b[^>]*\bid="toc"[^>]*>([\s\S]*?)<\/nav>/);
  const tocHtml = navMatch ? navMatch[1] : html;

  const tocIds = [];
  const tocIdRegex = /data-toc-id="([^"]*)"/g;
  let m;
  while ((m = tocIdRegex.exec(tocHtml)) !== null) {
    tocIds.push(m[1]);
  }
  if (tocIds.length === 0) return null;

  const headingIds = new Set();
  const headingIdRegex = /<h[23]\b[^>]*\sid="([^"]*)"/g;
  while ((m = headingIdRegex.exec(html)) !== null) {
    headingIds.add(m[1]);
  }

  const mismatches = tocIds.filter((id) => !headingIds.has(id));
  if (mismatches.length === 0) {
    return { file: filePath, hasToc: true, mismatch: false };
  }

  const headingIdList = Array.from(headingIds);
  const relPath = path.relative(distRoot, filePath);
  return {
    file: filePath,
    hasToc: true,
    mismatch: true,
    samples: mismatches.map((tocId) => ({
      page: '/' + relPath.replace(/index\.html$/, '').replace(/\\/g, '/'),
      tocId,
      closestHeadingId: closestId(tocId, headingIdList),
    })),
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const files = walk(args.dist);

  let totalTocPages = 0;
  let mismatchPages = 0;
  const allSamples = [];

  for (const file of files) {
    const result = auditFile(file, args.dist);
    if (!result || !result.hasToc) continue;
    totalTocPages++;
    if (result.mismatch) {
      mismatchPages++;
      allSamples.push(...result.samples);
    }
  }

  const mismatchRatio = totalTocPages > 0 ? mismatchPages / totalTocPages : 0;
  const top10 = allSamples.slice(0, 10);

  if (args.json) {
    console.log(
      JSON.stringify(
        {
          totalTocPages,
          mismatchPages,
          mismatchRatio,
          samples: top10,
        },
        null,
        2,
      ),
    );
    return;
  }

  console.log(`有 TOC 的頁數：${totalTocPages}`);
  console.log(
    `至少一條連結不符的頁數：${mismatchPages}（${(mismatchRatio * 100).toFixed(1)}%）`,
  );
  if (top10.length > 0) {
    console.log(`\n前 ${top10.length} 個不符樣本：`);
    for (const s of top10) {
      console.log(
        `  - ${s.page}  tocId="${s.tocId}"  最接近的實際 heading id="${s.closestHeadingId}"`,
      );
    }
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
