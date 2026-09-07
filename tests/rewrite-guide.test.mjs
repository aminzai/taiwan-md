import { marked } from 'marked';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import test from 'node:test';
import assert from 'node:assert/strict';
import {
  readFileSync,
  mkdtempSync,
  writeFileSync,
  mkdirSync,
  symlinkSync,
  rmSync,
} from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { Guide } from '../scripts/rewrite/engine.mjs';
import { renderRun } from '../scripts/rewrite/view.mjs';
function fixture(t) {
  const root = mkdtempSync(join(tmpdir(), 'rewrite-guide-'));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  writeFileSync(join(root, 'article.md'), 'Original article');
  writeFileSync(join(root, 'evidence.md'), 'Evidence');
  writeFileSync(join(root, 'draft.md'), 'Draft');
  const guide = new Guide(root);
  guide.start('article.md', { id: 'case', scope: 'section' });
  return { guide, root };
}
function submission(g) {
  const task = g.next('case');
  const input = task.submissionTemplate;
  input.actor = 'writer';
  input.artifacts = ['evidence.md'];
  for (const field of Object.keys(input.data))
    input.data[field] = 'Concrete explanation';
  if (task.stage === 'orient')
    input.data.candidateAngles = ['Explain the mechanism', 'Follow a person'];
  if (task.stage === 'investigate')
    input.data.claims = [
      {
        source: 'https://example.org',
        location: 'paragraph 1',
        support: 'A claim',
        doesNotSupport: 'All cases',
      },
    ];
  if (task.stage === 'verify')
    input.data.mechanicalChecks = [
      { command: 'fixture check', exitCode: 0, output: 'evidence.md' },
    ];
  if (task.stage === 'compose') {
    input.data.draftPath = 'draft.md';
    input.artifacts = ['draft.md'];
  }
  if (task.stage === 'cold-read') {
    input.data.contextDisclosure = 'fresh-context-draft-only';
    input.artifacts = ['draft.md'];
  }
  return input;
}
function review(g, verdict = 'accept') {
  return {
    ...g.next('case').reviewTemplate,
    actor: 'editor',
    verdict,
    rationale: 'Specific evidence supports this scoped decision',
    evidence: [{ path: 'evidence.md', location: 'line 1' }],
  };
}
function advance(g) {
  g.submit('case', submission(g));
  return g.review('case', review(g));
}
test('all six stages need external decisions; section never becomes a published article', (t) => {
  const { guide: g } = fixture(t);
  for (let i = 0; i < 6; i++) advance(g);
  const state = g.status('case');
  assert.equal(state.status, 'section-draft-ready');
  assert.equal(state.published, false);
  assert.equal(state.original.text, 'Original article');
  assert.equal(Object.keys(state.accepted).length, 6);
  assert.throws(() => g.submit('case', submission(g)), /not accepting/);
});
test('wrong stage, stale task, missing field, empty evidence and self review cannot advance', (t) => {
  const { guide: g } = fixture(t);
  assert.throws(
    () => g.submit('case', { ...submission(g), stage: 'release' }),
    /wrong stage/,
  );
  assert.throws(
    () => g.submit('case', { ...submission(g), revision: 99 }),
    /Stale task/,
  );
  const incomplete = submission(g);
  delete incomplete.data.readerQuestion;
  assert.throws(() => g.submit('case', incomplete), /Required field/);
  assert.throws(
    () => g.submit('case', { ...submission(g), artifacts: [] }),
    /artifact/,
  );
  assert.throws(() => g.submit('case', null), /JSON object/);
  g.submit('case', submission(g));
  assert.equal(g.status('case').stage, 'orient');
  assert.throws(
    () => g.review('case', { ...review(g), actor: 'writer' }),
    /different named actor/,
  );
  assert.throws(
    () => g.review('case', { ...review(g), submissionId: 'other' }),
    /Wrong submission/,
  );
  assert.throws(
    () => g.review('case', { ...review(g), evidence: [] }),
    /evidence locations/,
  );
  assert.equal(g.status('case').status, 'awaiting-review');
});
test('changed evidence blocks acceptance and backtracking invalidates downstream decisions', (t) => {
  const { guide: g, root } = fixture(t);
  advance(g);
  g.submit('case', submission(g));
  writeFileSync(join(root, 'evidence.md'), 'Changed evidence');
  assert.equal(g.next('case').action, 'backtrack');
  assert.throws(() => g.review('case', review(g)), /Dependencies changed/);
  assert.throws(
    () => g.backtrack('case', 'investigate', 'Evidence changed'),
    /backtrack to orient/,
  );
  g.backtrack('case', 'orient', 'Replace the unsupported premise');
  assert.deepEqual(g.status('case').accepted, {});
  assert.equal(g.status('case').submissions[0].artifacts[0].text, 'Evidence');
  assert.equal(g.status('case').stale.length, 0);
});
test('editing a draft invalidates composition onward without losing accepted research', (t) => {
  const { guide: g, root } = fixture(t);
  advance(g);
  advance(g);
  advance(g);
  writeFileSync(join(root, 'draft.md'), 'Revised draft');
  assert.throws(
    () => g.backtrack('case', 'cold-read', 'Reread'),
    /backtrack to compose/,
  );
  g.backtrack('case', 'compose', 'Correct the conclusion');
  assert.deepEqual(Object.keys(g.status('case').accepted), [
    'orient',
    'investigate',
  ]);
  assert.equal(g.status('case').stale.length, 0);
});
test('revise and block preserve history, and forward skipping is rejected', (t) => {
  const { guide: g } = fixture(t);
  assert.throws(() => g.backtrack('case', 'release', 'Skip'), /skip forward/);
  g.submit('case', submission(g));
  g.review('case', review(g, 'revise'));
  assert.equal(g.status('case').attempt, 2);
  g.submit('case', submission(g));
  g.review('case', review(g, 'block'));
  assert.equal(g.next('case').action, 'inspect-or-backtrack');
  assert.throws(() => g.submit('case', submission(g)), /not accepting/);
  g.backtrack('case', 'orient', 'New evidence resolves the block');
  assert.equal(g.status('case').submissions.length, 2);
});
test('cold reader must disclose the context boundary', (t) => {
  const { guide: g } = fixture(t);
  advance(g);
  advance(g);
  advance(g);
  assert.deepEqual(g.next('case').inputs, ['draft.md']);
  const input = submission(g);
  input.data.contextDisclosure = 'I read the blueprint';
  g.submit('case', input);
  assert.throws(() => g.review('case', review(g)), /new reader/);
  g.review('case', review(g, 'block'));
  assert.equal(g.status('case').status, 'blocked');
});
test('path escapes, unsafe ids, storage symlinks and concurrent writers fail closed', (t) => {
  const { guide: g, root } = fixture(t);
  assert.throws(() => g.load('../escape'), /Invalid run id/);
  assert.throws(() => g.load(undefined), /Invalid run id/);
  symlinkSync(tmpdir(), join(root, 'outside'));
  assert.throws(() => g.artifact('outside'), /inside the project/);
  const run = join(root, '.taiwanmd/rewrite-runs/case');
  mkdirSync(join(run, '.lock'));
  assert.throws(() => g.submit('case', submission(g)), /Run is locked/);
  rmSync(join(run, '.lock'), { recursive: true });
  symlinkSync(run, join(root, '.taiwanmd/rewrite-runs/alias'));
  assert.throws(() => g.load('alias'), /symbolic links/);
  rmSync(join(run, 'state.json'));
  symlinkSync(join(root, 'article.md'), join(run, 'state.json'));
  assert.throws(() => g.load('case'), /symbolic links/);
});
test('storage parent symlink is rejected before creating a run', (t) => {
  const root = mkdtempSync(join(tmpdir(), 'rewrite-store-'));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  writeFileSync(join(root, 'article.md'), 'text');
  symlinkSync(tmpdir(), join(root, '.taiwanmd'));
  assert.throws(() => new Guide(root).start('article.md'), /symbolic links/);
});
test('HTML export escapes submitted prose and review content', (t) => {
  const { guide: g } = fixture(t);
  const input = submission(g);
  input.data.readerQuestion = '<script>alert(1)</script>';
  g.submit('case', input);
  const html = renderRun(g.status('case'));
  assert.ok(html.includes('&lt;script&gt;'));
  assert.ok(!html.includes('<script>'));
  assert.equal((html.match(/<svg /g) || []).length, 6);
});

test('CLI returns machine-readable errors for malformed JSON and unknown commands', (t) => {
  const { root } = fixture(t);
  const bad = join(root, 'broken.json');
  writeFileSync(bad, '{broken');
  const cli = new URL('../scripts/rewrite/cli.mjs', import.meta.url);
  for (const args of [['submit', 'missing', bad], ['unknown-command']]) {
    const result = spawnSync(process.execPath, [fileURLToPath(cli), ...args], {
      encoding: 'utf8',
    });
    assert.equal(result.status, 1);
    assert.equal(typeof JSON.parse(result.stderr).error, 'string');
  }
});

test('dogfood references preserve both sources when adjacent citations are rendered', () => {
  const draft = readFileSync(
    new URL(
      '../reports/rewrite-guide/ezway-section/draft-v3.md',
      import.meta.url,
    ),
    'utf8',
  );
  const links = [...marked.parse(draft).matchAll(/href="([^"]+)"/g)].map(
    (match) => match[1],
  );
  assert.equal(links.length, 3);
  assert.equal(links[0], links[1]);
  assert.notEqual(links[1], links[2]);
});

test('review evidence is snapshotted and revocation invalidates its decision', (t) => {
  const { guide: g, root } = fixture(t);
  writeFileSync(join(root, 'review.md'), 'Accepted for this reason');
  g.submit('case', submission(g));
  const decision = {
    ...review(g),
    evidence: [{ path: 'review.md', location: 'line 1' }],
  };
  g.review('case', decision);
  writeFileSync(join(root, 'review.md'), 'REVOKED');
  assert.equal(g.status('case').stale[0].path, 'review.md');
  assert.equal(
    g.status('case').accepted.orient.review.artifacts[0].text,
    'Accepted for this reason',
  );
  assert.throws(
    () => g.backtrack('case', 'investigate', 'Reconsider'),
    /backtrack to orient/,
  );
  g.backtrack('case', 'orient', 'Reviewer revoked decision');
  g.submit('case', submission(g));
  assert.throws(
    () =>
      g.review('case', {
        ...review(g),
        evidence: [{ path: 'missing.md', location: 'line 1' }],
      }),
    /ENOENT/,
  );
});
test('empty containers and wrong types cannot masquerade as required material', (t) => {
  const { guide: g } = fixture(t);
  for (const [field, value] of [
    ['readerQuestion', false],
    ['subjectExplanation', []],
    ['candidateAngles', [null, null]],
    ['uncertainties', {}],
  ]) {
    const input = submission(g);
    input.data[field] = value;
    assert.throws(() => g.submit('case', input), /Required field/);
  }
});

test('next returns review guidance without embedding complete evidence snapshots', (t) => {
  const { guide: g, root } = fixture(t);
  writeFileSync(
    join(root, 'review.md'),
    'PRIVATE_FULL_REVIEW_MATERIAL '.repeat(2000),
  );
  g.submit('case', submission(g));
  g.review('case', {
    ...review(g, 'revise'),
    evidence: [{ path: 'review.md', location: 'paragraph 1' }],
  });
  const next = g.next('case');
  assert.equal(next.feedback.verdict, 'revise');
  assert.ok(!JSON.stringify(next).includes('PRIVATE_FULL_REVIEW_MATERIAL'));
  assert.ok(
    g
      .status('case')
      .submissions[0].review.artifacts[0].text.includes(
        'PRIVATE_FULL_REVIEW_MATERIAL',
      ),
  );
});
