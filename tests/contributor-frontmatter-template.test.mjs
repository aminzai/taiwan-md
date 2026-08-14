import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtemp, mkdir, readFile, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';

const REPO_ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const ARTICLE_PATH = 'knowledge/Culture/contributor-template.md';

test('CONTRIBUTING article template passes the strict frontmatter validator', async (t) => {
  const sandbox = await mkdtemp(join(tmpdir(), 'twmd-contributor-template-'));
  t.after(() => rm(sandbox, { recursive: true, force: true }));

  const contributing = await readFile(
    join(REPO_ROOT, 'CONTRIBUTING.md'),
    'utf8',
  );
  const section = contributing.split('### 文章結構範本', 2)[1];
  assert.ok(
    section,
    'CONTRIBUTING.md must contain the article template section',
  );

  const template = section.match(/```markdown\n([\s\S]*?)\n```/u)?.[1];
  assert.ok(
    template,
    'the article template must remain a fenced Markdown example',
  );

  const article = join(sandbox, ARTICLE_PATH);
  await mkdir(dirname(article), { recursive: true });
  await writeFile(article, `${template.trim()}\n`, 'utf8');

  const result = spawnSync(
    process.execPath,
    [join(REPO_ROOT, 'scripts/core/test-frontmatter.mjs'), '--strict'],
    {
      cwd: sandbox,
      env: { ...process.env, TWMD_VALIDATE_FILES: ARTICLE_PATH },
      encoding: 'utf8',
    },
  );

  assert.equal(result.status, 0, `${result.stdout}${result.stderr}`);
});
