#!/usr/bin/env node
/**
 * emit-sitemap-alias.mjs — 在 build 產物裡放一份 /sitemap.xml
 *
 * 誕生背景（2026-09-22 → 09-27）：爬蟲與人手打網址的慣例是先試 `/sitemap.xml`，
 * 而 Astro 的 @astrojs/sitemap 產的入口叫 `sitemap-index.xml`，站上 `/sitemap.xml`
 * 一直是 404。09-22 那次修補是在 `config/redirects-manual.txt` 寫一條 301，但這個
 * 站部署在 GitHub Pages，`_redirects` 是 Cloudflare Pages 的格式，GitHub Pages 不讀
 * 它——產生器重跑成功、檔案裡那一行也在，線上還是 404（LESSONS
 * `fix-lands-in-a-layer-the-platform-never-reads`）。
 *
 * 靜態站沒有伺服器可以發 301，所以接住這個慣例網址的唯一辦法是真的放一個檔案。
 * 這支就做這件事：把 `sitemap-index.xml` 原封不動複製成 `sitemap.xml`。sitemap
 * index 本身是合法的 sitemap 入口，內容是絕對網址，複製一份不會產生新的宣告。
 *
 * 刻意不寫成 meta-refresh HTML 或自己組 XML：前者不是 XML、爬蟲讀不懂，後者等於
 * 多一份會跟 Astro 產物漂移的手寫副本。複製才保證兩邊永遠逐字相同。
 *
 * fail-loud：找不到來源就 exit 1。安靜跳過等於讓 404 再活一輪，而這正是上一次
 * 修補失敗時沒有人發現的原因。
 *
 * Usage:
 *   node scripts/core/emit-sitemap-alias.mjs [distDir]   # 預設 dist
 */

import { copyFileSync, existsSync, statSync } from 'node:fs';
import { join, resolve } from 'node:path';

const distDir = resolve(process.argv[2] || 'dist');
const source = join(distDir, 'sitemap-index.xml');
const target = join(distDir, 'sitemap.xml');

if (!existsSync(source)) {
  console.error(
    `[sitemap-alias] 找不到 ${source}。@astrojs/sitemap 沒產出入口檔，或 distDir 給錯了。`,
  );
  process.exit(1);
}

copyFileSync(source, target);

const bytes = statSync(target).size;
console.log(
  `[sitemap-alias] /sitemap.xml ← sitemap-index.xml（${bytes} bytes）`,
);
