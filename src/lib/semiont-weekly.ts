/**
 * semiont-weekly.ts — Parser for Semiont weekly reports
 *
 * Reads weekly report files from reports/weekly/*.md at build time.
 * These files have NO YAML frontmatter; metadata lives in the H1 line.
 * Pattern mirrors src/lib/semiont-diary.ts — see that file for the diary
 * counterpart (docs/semiont/diary/*.md, session-suffixed filenames).
 *
 * Differences from the diary parser:
 * - Filenames are strictly `YYYY-MM-DD.md` (no session-letter suffix).
 * - `reports/weekly/dossier/` is a subdirectory (internal briefing, never
 *   sent to anyone per WEEKLY-REPORT-PIPELINE 鐵律 8) — `readdir` without
 *   recursion + the `.md` filter naturally excludes it.
 * - The weekly H1's leading blockquote/intro paragraph is real content
 *   (unlike diary, where it's stripped metadata), so the body is simply
 *   "everything after the H1 line".
 * - Only h2 headings are extracted for the TOC (weekly reports use a flat
 *   `## 1. …` … `## 10. …` section structure, no h3 subsections).
 * - Relative repo-internal links (e.g. `../evolution-roadmap-2026-07-10.md`)
 *   get rewritten to GitHub blob URLs so they don't 404 on the website —
 *   mirroring the same fix already shipped for the emailed edition
 *   (send-email-resend.py --web-url, see reports/semiont-weekly-section-2026-07-12.md).
 */

import { readdir, readFile, stat } from 'node:fs/promises';
import { resolve, join, posix } from 'node:path';
import { marked } from '../utils/marked-cjk.mjs';

// ── Types ──────────────────────────────────────────────

export interface WeeklyReport {
  /** ISO date string, e.g. "2026-07-12" (the Sunday the report was sent) */
  date: string;
  /** URL-safe slug — identical to `date` for weekly reports */
  slug: string;
  /** Original filename, e.g. "2026-07-12.md" */
  filename: string;
  /** ISO-8601 week label (Thursday rule), e.g. "W28" */
  weekLabel: string;
  /** Title extracted from H1, e.g. "🧬 Taiwan.md 週報 — 2026-07-05 ～ 2026-07-12" */
  title: string;
  /** Raw markdown body (everything after the H1 line) */
  bodyMarkdown: string;
  /** Rendered HTML */
  bodyHtml: string;
  /** Plain text excerpt (~140 chars) */
  excerpt: string;
  /** Chinese character count */
  wordCount: number;
  /** Extracted h2 headings for TOC */
  headings: { level: number; text: string; id: string }[];
  /** File mtime ms (CI git-restore-mtime → commit time) */
  mtimeMs: number;
}

// ── Filename parsing ───────────────────────────────────

function parseFilename(filename: string): string | null {
  // Strictly YYYY-MM-DD.md — no session suffix (unlike diary filenames)
  const match = filename.match(/^(\d{4}-\d{2}-\d{2})\.md$/);
  return match ? match[1] : null;
}

// ── ISO-8601 week number (Thursday rule) ───────────────

function getIsoWeekLabel(dateStr: string): string {
  const [y, m, d] = dateStr.split('-').map(Number);
  const date = new Date(Date.UTC(y, m - 1, d));
  const dayNum = date.getUTCDay() || 7; // Mon=1 … Sun=7
  date.setUTCDate(date.getUTCDate() + 4 - dayNum); // shift to this ISO week's Thursday
  const isoYear = date.getUTCFullYear();
  const yearStart = new Date(Date.UTC(isoYear, 0, 1));
  const weekNo = Math.ceil(
    ((date.getTime() - yearStart.getTime()) / 86400000 + 1) / 7,
  );
  return `W${weekNo}`;
}

// ── Content parsing ────────────────────────────────────

function parseContent(raw: string): {
  title: string;
  bodyMarkdown: string;
} {
  const lines = raw.split('\n');
  let title = '';
  let bodyStartIndex = 0;

  // Parse H1: "# 🧬 Taiwan.md 週報 — 2026-07-05 ～ 2026-07-12" (free-form —
  // everything after "# " is the title, unlike diary's structured H1).
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    if (line.startsWith('# ')) {
      title = line.slice(2).trim();
      bodyStartIndex = i + 1;
      break;
    }
  }

  // Everything after the H1 is body — weekly reports' leading blockquote/
  // italic intro paragraph is real content, not metadata to strip.
  const bodyMarkdown = lines.slice(bodyStartIndex).join('\n');
  return { title, bodyMarkdown };
}

// ── Link rewriting ──────────────────────────────────────

const WEEKLY_REPORTS_BASE = 'reports/weekly/';
const GITHUB_BLOB_PREFIX =
  'https://github.com/frank890417/taiwan-md/blob/main/';

function rewriteHref(href: string): string {
  if (!href) return href;
  if (
    href.startsWith('http://') ||
    href.startsWith('https://') ||
    href.startsWith('mailto:') ||
    href.startsWith('#')
  ) {
    return href;
  }
  if (href.startsWith('/')) {
    return href;
  }
  // Relative repo-internal link, e.g. "../evolution-roadmap-2026-07-10.md"
  // → resolve against reports/weekly/ then point at the GitHub blob view
  // (rendering it as a site-relative route would 404).
  const resolved = posix.normalize(WEEKLY_REPORTS_BASE + href);
  // Defensive: if the relative path tried to escape above repo root, drop
  // the leftover leading "../" so we don't build a malformed GitHub URL.
  const stripped = resolved.replace(/^(\.\.\/)+/, '');
  return GITHUB_BLOB_PREFIX + stripped;
}

// ── Markdown rendering ─────────────────────────────────

function createRenderer(): marked.Renderer {
  const renderer = new marked.Renderer();

  // tokens → parseInline（同 article-render.ts）：`text` 是未解析原文，
  // 直接吐會把 `**` 印在標題裡。id 仍取原文，錨點不變。
  renderer.heading = function ({ text, tokens, depth }) {
    const id = text
      .toLowerCase()
      .replace(/\s+/g, '-')
      .replace(/[^\w一-鿿-]/g, '')
      .slice(0, 60);
    return `<h${depth} id="${id}">${this.parser.parseInline(tokens)}</h${depth}>\n`;
  };

  renderer.link = ({ href, title, text }) => {
    const finalHref = rewriteHref(href || '');
    // isExternal is checked against the FINAL href (post-rewrite): both
    // original http(s) links and rewritten GitHub blob links are off-site.
    const isExternal =
      finalHref.startsWith('http://') || finalHref.startsWith('https://');
    const titleAttr = title ? ` title="${title}"` : '';
    const targetAttr = isExternal
      ? ' target="_blank" rel="noopener noreferrer"'
      : '';
    return `<a href="${finalHref}"${titleAttr}${targetAttr}>${text}</a>`;
  };

  return renderer;
}

function extractHeadings(
  html: string,
): { level: number; text: string; id: string }[] {
  // h2 only — weekly reports use a flat "## 1. …" section structure.
  const headings: { level: number; text: string; id: string }[] = [];
  const regex = /<h2[^>]*(?:id="([^"]*)")?[^>]*>(.*?)<\/h2>/gi;
  let match;
  while ((match = regex.exec(html)) !== null) {
    const existingId = match[1];
    const rawText = match[2].replace(/<[^>]+>/g, '').trim();
    const id =
      existingId ||
      rawText
        .toLowerCase()
        .replace(/\s+/g, '-')
        .replace(/[^\w一-鿿-]/g, '')
        .slice(0, 60);
    if (rawText) headings.push({ id, text: rawText, level: 2 });
  }
  return headings;
}

function makeExcerpt(markdown: string, maxLen = 140): string {
  // Strip markdown formatting, take first meaningful paragraph.
  // Same approach as semiont-diary.ts's makeExcerpt, plus underscore-italic
  // stripping: weekly reports open with a `_…_` (not `*…*`) intro paragraph.
  const plain = markdown
    .replace(/^#+\s+.*/gm, '') // headings
    .replace(/\*\*(.+?)\*\*/g, '$1') // bold
    .replace(/\*(.+?)\*/g, '$1') // italic (asterisk)
    .replace(/_(.+?)_/g, '$1') // italic (underscore) — weekly intro/footer convention
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') // links
    .replace(/`[^`]+`/g, '') // inline code
    .replace(/^>\s+/gm, '') // blockquotes
    .replace(/^[-*]\s+/gm, '') // list items
    .replace(/\n{2,}/g, '\n')
    .trim();

  const firstParagraph =
    plain.split('\n').find((l) => l.trim().length > 20) || plain;
  if (firstParagraph.length <= maxLen) return firstParagraph;
  return (
    firstParagraph.slice(0, maxLen).replace(/[，。、；：！？\s]+$/, '') + '⋯'
  );
}

function countWords(markdown: string): number {
  const plain = markdown
    .replace(/```[\s\S]*?```/g, '')
    .replace(/`[^`]+`/g, '')
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    .replace(/[#*_>`\-|]/g, '')
    .replace(/\n/g, '');
  return plain.length;
}

// ── Public API ─────────────────────────────────────────

const WEEKLY_DIR = resolve(process.cwd(), 'reports/weekly');

export async function getAllWeeklyReports(): Promise<WeeklyReport[]> {
  const renderer = createRenderer();
  const files = await readdir(WEEKLY_DIR);
  const mdFiles = files
    .filter((f) => f.endsWith('.md'))
    .map((f) => f.normalize('NFC'));

  const reports: WeeklyReport[] = [];

  for (const file of mdFiles) {
    const date = parseFilename(file);
    if (!date) continue; // Skip filenames that don't match YYYY-MM-DD.md

    const filePath = join(WEEKLY_DIR, file);
    const raw = await readFile(filePath, 'utf-8');
    const { title, bodyMarkdown } = parseContent(raw);

    if (!title) continue; // Skip files that don't parse

    const fileStat = await stat(filePath);

    const bodyHtml = marked.parse(bodyMarkdown, {
      renderer,
      breaks: true,
    }) as string;
    const headings = extractHeadings(bodyHtml);
    const excerpt = makeExcerpt(bodyMarkdown);
    const wordCount = countWords(bodyMarkdown);

    reports.push({
      date,
      slug: date,
      filename: file,
      weekLabel: getIsoWeekLabel(date),
      title,
      bodyMarkdown,
      bodyHtml,
      excerpt,
      wordCount,
      headings,
      mtimeMs: fileStat.mtimeMs,
    });
  }

  // Sort: newest first (slug === date, so a plain string sort suffices —
  // no Greek-order tie-breaker needed like diary's multi-session-per-day).
  reports.sort((a, b) => b.date.localeCompare(a.date));

  return reports;
}

export function estimateReadingTime(wordCount: number): number {
  // Chinese reading speed ~400-500 chars/min
  return Math.max(1, Math.ceil(wordCount / 450));
}
