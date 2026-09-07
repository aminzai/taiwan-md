import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { execFileSync } from 'node:child_process';
import {
  classifyFiles,
  collectFiles,
} from '../scripts/tools/pr-changed-files.mjs';

test('git paths survive Chinese, spaces, quotes, shell syntax and newline; hubs excluded explicitly', () => {
  const cwd = mkdtempSync(join(tmpdir(), 'pr-files-'));
  const git = (...args) =>
    execFileSync('git', args, {
      cwd,
      encoding: 'utf8',
      stdio: ['ignore', 'pipe', 'pipe'],
    }).trim();
  const write = (f) => {
    mkdirSync(dirname(join(cwd, f)), { recursive: true });
    writeFileSync(join(cwd, f), 'test');
  };
  try {
    git('init');
    git('config', 'user.email', 'test@example.com');
    git('config', 'user.name', 'Test');
    write('initial');
    git('add', '.');
    git('commit', '-m', 'base');
    const base = git('rev-parse', 'HEAD');
    const files = [
      'knowledge/Society/中文 空白.md',
      'knowledge/People/"${bad}`.md',
      'knowledge/Art/new\nline.md',
      'knowledge/People/_People Hub.md',
      'knowledge/_translations.json',
    ];
    files.forEach(write);
    git('add', '.');
    git('commit', '-m', 'change');
    const selected = collectFiles(base, 'HEAD', cwd);
    assert.deepEqual(new Set(selected), new Set(files));
    const m = classifyFiles(selected, cwd);
    assert.equal(m.content.length, 3);
    assert.equal(m.excluded.length, 1);
    assert.equal(m.pr_type, 'mixed');
    assert.equal(classifyFiles([files[3]], cwd).all_kn.length, 0);
    assert.deepEqual(collectFiles('HEAD', 'HEAD', cwd), []);
    assert.throws(() => classifyFiles(['knowledge/People/missing.md'], cwd));
    git('rm', files[0]);
    git('mv', files[1], 'knowledge/People/renamed.md');
    git('commit', '-m', 'rename-delete');
    assert.deepEqual(
      new Set(collectFiles('HEAD^', 'HEAD', cwd)),
      new Set(['knowledge/People/renamed.md']),
    );
  } finally {
    rmSync(cwd, { recursive: true, force: true });
  }
});

test('fork checkout uses merge parents only when requested refs are unavailable', () => {
  const cwd = mkdtempSync(join(tmpdir(), 'pr-fork-'));
  const git = (...args) =>
    execFileSync('git', args, {
      cwd,
      encoding: 'utf8',
      stdio: ['ignore', 'pipe', 'pipe'],
    }).trim();
  try {
    git('init');
    git('config', 'user.email', 'test@example.com');
    git('config', 'user.name', 'Test');
    writeFileSync(join(cwd, 'base'), 'base');
    git('add', '.');
    git('commit', '-m', 'base');
    git('checkout', '-b', 'fork');
    writeFileSync(join(cwd, 'fork file'), 'fork');
    git('add', '.');
    git('commit', '-m', 'fork');
    git('checkout', '-b', 'target', 'HEAD^');
    writeFileSync(join(cwd, 'target'), 'target');
    git('add', '.');
    git('commit', '-m', 'target');
    git('merge', '--no-ff', 'fork', '-m', 'merge');
    assert.deepEqual(
      collectFiles('unavailable-base', 'unavailable-head', cwd),
      ['fork file'],
    );
    assert.deepEqual(collectFiles('HEAD', 'HEAD', cwd), []);
  } finally {
    rmSync(cwd, { recursive: true, force: true });
  }
});

test('frontmatter validation scans lowercase legacy resource directories', () => {
  const cwd = mkdtempSync(join(tmpdir(), 'fm-paths-'));
  try {
    const file = 'knowledge/vi/resources/example.md';
    mkdirSync(dirname(join(cwd, file)), { recursive: true });
    writeFileSync(
      join(cwd, file),
      '---\ntitle: Example\ndescription: A resource description\ndate: 2026-09-07\ntags: [resource]\ntranslatedFrom: Technology/source.md\n---\nBody\n',
    );
    mkdirSync(join(cwd, 'knowledge/Technology'), { recursive: true });
    writeFileSync(join(cwd, 'knowledge/Technology/source.md'), 'source');
    const manifest = join(cwd, 'files.json');
    writeFileSync(manifest, JSON.stringify([file]));
    const result = execFileSync(
      process.execPath,
      [
        new URL('../scripts/core/test-frontmatter.mjs', import.meta.url)
          .pathname,
      ],
      {
        cwd,
        encoding: 'utf8',
        env: { ...process.env, TWMD_VALIDATE_FILES_JSON: manifest },
      },
    );
    assert.match(result, /1 files scanned/);
    assert.match(result, /passed: 1\/1/);
  } finally {
    rmSync(cwd, { recursive: true, force: true });
  }
});
