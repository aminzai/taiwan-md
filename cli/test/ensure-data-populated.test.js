/**
 * Tests for isPopulatedKnowledgeDir() in lib/ensure-data.js — issue #1790.
 *
 * Why this file exists: the readiness check used to ask "is there at least one
 * subdirectory", and `.git` is a subdirectory. An interrupted
 * `git clone --sparse` leaves `~/.taiwanmd/knowledge/.git` and nothing else,
 * so the check passed, the follow-up sync was skipped, and the MCP server kept
 * reporting `ready on stdio` while every article lookup returned nothing.
 * `stats` showed `totalArticles: 0` next to `dataFreshness: "live-repo"` — the
 * healthy value — so there was no signal anywhere that the knowledge base was
 * empty.
 *
 * The invariant being pinned: this function answers "can a reader get an
 * article out of here", not "is there anything here at all".
 *
 * Run with: cd cli && npx vitest run test/ensure-data-populated.test.js
 */

import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import fs from 'fs';
import os from 'os';
import path from 'path';
import { isPopulatedKnowledgeDir } from '../src/lib/ensure-data.js';

let tmp;

beforeEach(() => {
  tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'twmd-ensure-data-'));
});

afterEach(() => {
  fs.rmSync(tmp, { recursive: true, force: true });
});

describe('isPopulatedKnowledgeDir', () => {
  it('rejects a directory holding only .git (the #1790 interrupted clone)', () => {
    fs.mkdirSync(path.join(tmp, '.git', 'objects'), { recursive: true });
    fs.writeFileSync(path.join(tmp, '.git', 'HEAD'), 'ref: refs/heads/main\n');
    expect(isPopulatedKnowledgeDir(tmp)).toBe(false);
  });

  it('rejects an empty directory', () => {
    expect(isPopulatedKnowledgeDir(tmp)).toBe(false);
  });

  it('rejects a directory that does not exist', () => {
    expect(isPopulatedKnowledgeDir(path.join(tmp, 'nope'))).toBe(false);
  });

  it('rejects null/empty input rather than throwing', () => {
    expect(isPopulatedKnowledgeDir('')).toBe(false);
    expect(isPopulatedKnowledgeDir(null)).toBe(false);
  });

  it('rejects category directories that contain no .md files', () => {
    // A sparse checkout that created the folders but fetched no blobs.
    fs.mkdirSync(path.join(tmp, 'knowledge', 'People'), { recursive: true });
    fs.mkdirSync(path.join(tmp, 'knowledge', 'Food'), { recursive: true });
    expect(isPopulatedKnowledgeDir(tmp)).toBe(false);
  });

  it('accepts the nested layout that sync actually produces', () => {
    // `sync` clones the repo *into* ~/.taiwanmd/knowledge/, so articles land
    // one level deeper.
    fs.mkdirSync(path.join(tmp, 'knowledge', 'Food'), { recursive: true });
    fs.writeFileSync(
      path.join(tmp, 'knowledge', 'Food', '珍珠奶茶.md'),
      '---\ntitle: 珍珠奶茶\n---\n',
    );
    expect(isPopulatedKnowledgeDir(tmp)).toBe(true);
  });

  it('accepts a flat layout, so an older or future sync still resolves', () => {
    fs.mkdirSync(path.join(tmp, 'Food'), { recursive: true });
    fs.writeFileSync(path.join(tmp, 'Food', '滷肉飯.md'), '# 滷肉飯\n');
    expect(isPopulatedKnowledgeDir(tmp)).toBe(true);
  });

  it('is not fooled by .md files sitting loose at the root', () => {
    // README.md at the clone root is not an article; articles live in
    // category directories.
    fs.writeFileSync(path.join(tmp, 'README.md'), '# Taiwan.md\n');
    expect(isPopulatedKnowledgeDir(tmp)).toBe(false);
  });

  it('ignores dot-directories even when they contain .md files', () => {
    fs.mkdirSync(path.join(tmp, '.github'), { recursive: true });
    fs.writeFileSync(
      path.join(tmp, '.github', 'PULL_REQUEST_TEMPLATE.md'),
      '# PR\n',
    );
    expect(isPopulatedKnowledgeDir(tmp)).toBe(false);
  });

  it('accepts a real clone root, where articles are nested and .git is present', () => {
    // The healthy post-sync state: both .git and knowledge/<Cat>/*.md.
    fs.mkdirSync(path.join(tmp, '.git'), { recursive: true });
    fs.mkdirSync(path.join(tmp, 'knowledge', 'Technology'), {
      recursive: true,
    });
    fs.writeFileSync(
      path.join(tmp, 'knowledge', 'Technology', 'Computex.md'),
      '# Computex\n',
    );
    expect(isPopulatedKnowledgeDir(tmp)).toBe(true);
  });
});
