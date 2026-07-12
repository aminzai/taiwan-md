/** Post-run contract for a strict Rewrite Pipeline spawn.
 *
 * Runs inside the isolated worktree before it is merged. A model exiting 0 is
 * not evidence that the canonical pipeline passed; these executable receipts
 * are. Any failure keeps the worktree for inspection and blocks main.
 */

import { existsSync, readFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { isAbsolute, join, relative, resolve } from 'node:path';
import type { Task } from '../tasks/types.ts';

export interface StrictRewriteResult {
  passed: boolean;
  articleFiles: string[];
  checks: { name: string; passed: boolean; detail: string }[];
}

function run(cwd: string, command: string, args: string[]) {
  const result = spawnSync(command, args, {
    cwd,
    encoding: 'utf8',
    timeout: 10 * 60_000,
  });
  return {
    passed: result.status === 0,
    detail:
      `${command} ${args.join(' ')}\n${result.stdout ?? ''}${result.stderr ?? ''}`.trim(),
  };
}

function frontmatterValue(body: string, key: string): string | null {
  const frontmatter = body.match(/^---\s*\n([\s\S]*?)\n---/m)?.[1] ?? '';
  const match = frontmatter.match(
    new RegExp(`^${key}:\\s*['\"]?([^'\"\\n]+)['\"]?\\s*$`, 'm'),
  );
  return match?.[1]?.trim() ?? null;
}

export function verifyStrictRewrite(
  task: Task,
  worktreePath: string,
  baseRef: string,
): StrictRewriteResult {
  const checks: StrictRewriteResult['checks'] = [];
  const add = (name: string, passed: boolean, detail: string) =>
    checks.push({ name, passed, detail });

  const changed = run(worktreePath, 'git', [
    'diff',
    '--name-only',
    '--diff-filter=ACMR',
    `${baseRef}...HEAD`,
  ]);
  add('changed-files-readable', changed.passed, changed.detail);
  const files = changed.detail
    .split('\n')
    .filter((line) => !line.startsWith('git diff '))
    .map((line) => line.trim())
    .filter(Boolean);
  const articleFiles = files.filter(
    (file) => file.startsWith('knowledge/') && file.endsWith('.md'),
  );
  add(
    'exactly-one-article',
    articleFiles.length === 1,
    `expected exactly 1 changed knowledge article; found ${articleFiles.length}: ${articleFiles.join(', ') || '(none)'}`,
  );

  const articleRel = articleFiles[0];
  if (articleRel) {
    const articleAbs = join(worktreePath, articleRel);
    const article = existsSync(articleAbs)
      ? readFileSync(articleAbs, 'utf8')
      : '';
    const reportRaw = frontmatterValue(article, 'researchReport');
    const reportRel = reportRaw
      ? relative(
          worktreePath,
          isAbsolute(reportRaw) ? reportRaw : resolve(worktreePath, reportRaw),
        )
      : null;
    const reportAbs = reportRel ? join(worktreePath, reportRel) : '';
    add(
      'research-report-linked',
      Boolean(reportRel && existsSync(reportAbs)),
      reportRel ?? 'frontmatter researchReport is missing',
    );

    if (reportRel && existsSync(reportAbs)) {
      const reportStem = reportRel.replace(/\.md$/, '');
      for (const stage of ['35', '36']) {
        const auditRel = `${reportStem}-stage${stage}-audit.md`;
        const auditAbs = join(worktreePath, auditRel);
        const auditBody = existsSync(auditAbs)
          ? readFileSync(auditAbs, 'utf8')
          : '';
        add(
          `stage-${stage}-audit`,
          existsSync(auditAbs) && /\bPASS\b/.test(auditBody),
          auditRel,
        );
      }
      const research = run(worktreePath, 'python3', [
        'scripts/tools/research-report-health.py',
        reportRel,
        '--tier=depth',
      ]);
      add('research-report-health-depth', research.passed, research.detail);
    }

    for (const profile of ['rewrite-stage-3-5', 'rewrite-stage-4']) {
      const health = run(worktreePath, 'python3', [
        'scripts/tools/article-health.py',
        articleRel,
        `--profile=${profile}`,
      ]);
      add(`article-health-${profile}`, health.passed, health.detail);
    }

    const comparison = run(worktreePath, 'python3', [
      'scripts/tools/compare-article-quality.py',
      articleRel,
      '--limit=5',
      '--output',
      join(task.folder_path, 'outputs', 'quality-comparison.md'),
    ]);
    add(
      'recent-article-quality-comparison',
      comparison.passed,
      comparison.detail,
    );
  }

  const statusPath = join(task.folder_path, 'status.log');
  const status = existsSync(statusPath) ? readFileSync(statusPath, 'utf8') : '';
  add(
    'status-receipts',
    /Stage 3\.5:\s*PASS/i.test(status) && /Stage 3\.6:\s*PASS/i.test(status),
    existsSync(statusPath) ? `checked ${statusPath}` : `missing ${statusPath}`,
  );

  return {
    passed: checks.every((check) => check.passed),
    articleFiles,
    checks,
  };
}

export function formatStrictRewriteResult(result: StrictRewriteResult): string {
  return [
    '# Strict Rewrite Pipeline verification',
    ...result.checks.map(
      (check) =>
        `${check.passed ? 'PASS' : 'FAIL'} ${check.name}\n${check.detail}`,
    ),
    `RESULT: ${result.passed ? 'PASS' : 'FAIL'}`,
  ].join('\n\n');
}
