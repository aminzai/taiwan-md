/** Lossless PR path transport. Only scalar counts/status enter Actions outputs. */
import { execFileSync } from 'node:child_process';
import { existsSync, writeFileSync, appendFileSync } from 'node:fs';
import { basename, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { ALL_LANGUAGE_CODES } from '../../src/config/languages.mjs';

export function classifyFiles(all, cwd = process.cwd()) {
  const translations = new Set(ALL_LANGUAGE_CODES.filter((x) => x !== 'zh-TW'));
  const markdown = (f) => /^(knowledge|src\/content)\/[\s\S]*\.md$/.test(f);
  const excluded = all.filter(
    (f) => markdown(f) && basename(f).startsWith('_'),
  );
  const content = all.filter(
    (f) => markdown(f) && !basename(f).startsWith('_'),
  );
  for (const f of content) {
    if (!existsSync(resolve(cwd, f)))
      throw new Error(`Selected PR file is missing: ${JSON.stringify(f)}`);
  }
  const all_kn = content.filter((f) => f.startsWith('knowledge/'));
  const isTranslation = (f) =>
    translations.has(f.split('/')[f.startsWith('knowledge/') ? 1 : 2]);
  const zh_kn = all_kn.filter((f) => !isTranslation(f));
  const engineering = all.filter((f) => !markdown(f));
  const pr_type = !content.length
    ? 'engineering'
    : engineering.length
      ? 'mixed'
      : content.every(isTranslation)
        ? 'translation'
        : 'content';
  return { all, content, all_kn, zh_kn, excluded, pr_type };
}
export function collectFiles(base, head, cwd = process.cwd()) {
  const diff = (range) =>
    execFileSync(
      'git',
      ['diff', '--name-only', '-z', '--diff-filter=ACMR', range, '--'],
      { cwd, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] },
    )
      .split('\0')
      .filter(Boolean);
  if (!base || !head)
    throw new Error('PR_BASE_SHA and PR_HEAD_SHA are required');
  try {
    return diff(`${base}...${head}`);
  } catch (error) {
    // A valid empty diff is not a failure. Only missing refs can use merge parents.
    try {
      execFileSync('git', ['rev-parse', '--verify', 'HEAD^2'], {
        cwd,
        stdio: 'ignore',
      });
    } catch {
      throw error;
    }
    return diff('HEAD^1...HEAD^2');
  }
}
if (
  process.argv[1] &&
  import.meta.url === pathToFileURL(resolve(process.argv[1])).href
) {
  const manifest = classifyFiles(
    collectFiles(process.env.PR_BASE_SHA, process.env.PR_HEAD_SHA),
  );
  writeFileSync(
    '.pr-changed-files.json',
    JSON.stringify(manifest, null, 2) + '\n',
  );
  if (process.env.GITHUB_OUTPUT)
    appendFileSync(
      process.env.GITHUB_OUTPUT,
      `pr_type=${manifest.pr_type}\ncount=${manifest.all_kn.length}\n`,
    );
  console.log(
    JSON.stringify({
      type: manifest.pr_type,
      articles: manifest.content.length,
      excluded: manifest.excluded.length,
    }),
  );
}
