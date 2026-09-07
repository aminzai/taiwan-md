"""PR review preserves existing curation but rejects new self-promotion."""
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]


def test_existing_featured_and_lowercase_translation_category(tmp_path):
    for rel in ('scripts/tools/review-pr.sh', 'src/config/languages.mjs'):
        target = tmp_path / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / rel, target)
    (tmp_path / 'knowledge/resources').mkdir(parents=True)
    article = tmp_path / 'knowledge/resources/sample.md'
    translation = tmp_path / 'knowledge/vi/resources/sample.md'
    translation.parent.mkdir(parents=True)
    body = '\n'.join(f'段落 {n}：2026 年的研究資料與具體說明。' for n in range(15))
    article.write_text('---\ntitle: Sample\ndescription: Example\ndate: 2026-09-07\ntags: [test]\nfeatured: true\n---\n## Heading\n' + body + '\nhttps://example.com\n')
    translation.write_text(article.read_text().replace('featured: true', 'translatedFrom: Resources/sample.md'))
    def git(*args):
        return subprocess.check_output(['git', *args], cwd=tmp_path, text=True).strip()
    git('init', '-q')
    git('-c', 'user.name=Test', '-c', 'user.email=test@example.com', 'add', '.')
    git('-c', 'user.name=Test', '-c', 'user.email=test@example.com', 'commit', '-qm', 'base')
    base = git('rev-parse', 'HEAD')
    def review(paths, ref):
        return subprocess.run(['bash', 'scripts/tools/review-pr.sh', *paths], cwd=tmp_path, env={**os.environ, 'PR_BASE_SHA': ref}, text=True, capture_output=True)
    existing = review(['knowledge/resources/sample.md', 'knowledge/vi/resources/sample.md'], base)
    assert existing.returncode == 0, existing.stdout + existing.stderr
    assert '無效 category' not in existing.stdout
    new = tmp_path / 'knowledge/resources/new.md'
    new.write_text(article.read_text())
    for ref in (base, '', 'missing-ref'):
        result = review(['knowledge/resources/new.md'], ref)
        assert result.returncode != 0
        assert '不可新增 featured' in result.stdout
