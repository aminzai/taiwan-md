#!/usr/bin/env node
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { Guide } from './engine.mjs';
import { renderRun } from './view.mjs';
const root = resolve(dirname(fileURLToPath(import.meta.url)), '../..');
const guide = new Guide(root);
const [command, ...args] = process.argv.slice(2);
const option = (name) => {
  const i = args.indexOf(name);
  return i < 0 ? undefined : args[i + 1];
};
try {
  let result;
  switch (command) {
    case 'start':
      result = guide.start(args[0], {
        scope: option('--scope'),
        id: option('--id'),
      });
      break;
    case 'next':
      result = guide.next(args[0]);
      break;
    case 'status':
      result = guide.status(args[0]);
      break;
    case 'submit':
      result = guide.submit(args[0], JSON.parse(readFileSync(args[1], 'utf8')));
      break;
    case 'review':
      result = guide.review(args[0], JSON.parse(readFileSync(args[1], 'utf8')));
      break;
    case 'backtrack':
      result = guide.backtrack(args[0], args[1], option('--reason'));
      break;
    case 'export': {
      if (!args[1]) throw new Error('Output HTML path required');
      writeFileSync(args[1], renderRun(guide.status(args[0])), { flag: 'wx' });
      result = { exported: resolve(args[1]), snapshot: true };
      break;
    }
    case undefined:
    case 'help':
    case '--help':
      result = {
        tool: 'Rewrite Guide',
        commands: [
          'start <article-path> [--scope article|section] [--id run-id]',
          'next <run-id>',
          'submit <run-id> <submission.json>',
          'review <run-id> <review.json>',
          'backtrack <run-id> <stage> --reason <reason>',
          'status <run-id>',
          'export <run-id> <output.html>',
        ],
        note: 'JSON protocol. AI/humans provide editorial judgments; no automatic publication.',
      };
      break;
    default:
      throw new Error(`Unknown command: ${command}`);
  }
  process.stdout.write(JSON.stringify(result, null, 2) + '\n');
} catch (error) {
  process.stderr.write(JSON.stringify({ error: error.message }) + '\n');
  process.exitCode = 1;
}
