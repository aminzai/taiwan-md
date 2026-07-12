/**
 * Pure formatting helpers — relative time, color tokens per status,
 * type emojis. No Solid/Astro imports so this stays unit-testable.
 */

import type { TaskPriority, TaskStatus, TaskType } from './types';

const TYPE_EMOJI: Record<string, string> = {
  'article-rewrite': '📝',
  'article-new': '✨',
  'article-evolve': '🌿',
  'spore-publish': '🌱',
  'spore-harvest': '🍂',
  'pr-review': '🔍',
  'issue-handle': '🐛',
  'data-refresh': '🔄',
  'status-report': '📊',
  'self-diagnose': '🩺',
  heartbeat: '💗',
};

export function typeEmoji(type: TaskType | string): string {
  return TYPE_EMOJI[type] ?? '📦';
}

const STATUS_CLASSES: Record<TaskStatus, string> = {
  pending: 'bg-accent-blue/15 text-accent-blue border border-accent-blue/30',
  spawning:
    'bg-accent-amber/15 text-accent-amber border border-accent-amber/30',
  'in-progress':
    'bg-accent-amber/15 text-accent-amber border border-accent-amber/30',
  blocked:
    'bg-accent-orange/15 text-accent-orange border border-accent-orange/30',
  done: 'bg-accent-green/15 text-accent-green-soft border border-accent-green/30',
  failed: 'bg-accent-red/15 text-accent-red border border-accent-red/30',
  retired: 'bg-bg-raised text-text-muted border border-line',
  'awaiting-cheyu':
    'bg-accent-purple/15 text-accent-purple border border-accent-purple/30',
};

export function statusBadgeClass(status: TaskStatus | string): string {
  return (
    STATUS_CLASSES[status as TaskStatus] ??
    'bg-bg-raised text-text-muted border border-line'
  );
}

const PRIORITY_CLASSES: Record<TaskPriority, string> = {
  P0: 'bg-accent-red/15 text-accent-red border border-accent-red/30',
  P1: 'bg-accent-orange/15 text-accent-orange border border-accent-orange/30',
  P2: 'bg-accent-amber/15 text-accent-amber border border-accent-amber/30',
  P3: 'bg-bg-raised text-text-secondary border border-line',
};

export function priorityBadgeClass(priority: TaskPriority | string): string {
  return (
    PRIORITY_CLASSES[priority as TaskPriority] ??
    'bg-bg-raised text-text-muted border border-line'
  );
}

const PRIORITY_RANK: Record<string, number> = { P0: 0, P1: 1, P2: 2, P3: 3 };
export function priorityRank(p: string): number {
  return PRIORITY_RANK[p] ?? 99;
}

export function relativeTime(iso: string | undefined): string {
  if (!iso) return '—';
  const t = new Date(iso).getTime();
  if (Number.isNaN(t)) return iso;
  const diff = Date.now() - t;
  const abs = Math.abs(diff);
  const minute = 60 * 1000;
  const hour = 60 * minute;
  const day = 24 * hour;
  const future = diff < 0;
  const fmt = (n: number, unit: string): string =>
    future ? `in ${n}${unit}` : `${n}${unit} ago`;
  if (abs < minute) return future ? 'soon' : 'just now';
  if (abs < hour) return fmt(Math.round(abs / minute), 'm');
  if (abs < day) return fmt(Math.round(abs / hour), 'h');
  if (abs < 30 * day) return fmt(Math.round(abs / day), 'd');
  return new Date(iso).toLocaleDateString('zh-TW');
}

/** "12s" / "4m 12s" / "1h 04m" — elapsed since iso, compact. */
export function elapsedSince(iso: string | undefined): string {
  if (!iso) return '—';
  const start = new Date(iso).getTime();
  if (Number.isNaN(start)) return '—';
  const ms = Math.max(0, Date.now() - start);
  const sec = Math.floor(ms / 1000);
  if (sec < 60) return `${sec}s`;
  const min = Math.floor(sec / 60);
  const remSec = sec % 60;
  if (min < 60)
    return remSec > 0
      ? `${min}m ${remSec.toString().padStart(2, '0')}s`
      : `${min}m`;
  const hr = Math.floor(min / 60);
  const remMin = min % 60;
  return `${hr}h ${remMin.toString().padStart(2, '0')}m`;
}

export function formatLocalDate(d: Date = new Date()): string {
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${y}-${m}-${day}`;
}

export function formatDateTime(iso: string | undefined): string {
  if (!iso) return '—';
  try {
    return new Date(iso).toLocaleString('zh-TW', { hour12: false });
  } catch {
    return iso;
  }
}

const TREND_ARROW: Record<string, string> = {
  up: '↑',
  down: '↓',
  flat: '→',
};
export function trendArrow(t: string | undefined): string {
  if (!t) return '—';
  return TREND_ARROW[t] ?? '→';
}

export function trendClass(t: string | undefined): string {
  if (t === 'up') return 'text-accent-green-soft';
  if (t === 'down') return 'text-accent-red';
  return 'text-text-secondary';
}

/**
 * Phase 5.1 / 5.2 — derive a short engine/model badge for a task.
 * Source: task.inputs.engine + task.inputs.model, falling back to type-default.
 * Phase 5.2 (2026-07-12): default engine is grok (mirrors backend).
 */
/** Default engine when task.inputs.engine is unset (Phase 5.2). */
export const DEFAULT_ENGINE = 'grok';

const DEFAULT_GROK_MODEL_BY_TYPE: Record<string, string> = {
  'lang-sync-refresh': 'grok-composer-2.5-fast',
  'lang-sync-translate': 'grok-composer-2.5-fast',
  'data-refresh': 'grok-composer-2.5-fast',
  'format-check': 'grok-composer-2.5-fast',
  'status-report': 'grok-composer-2.5-fast',
  'article-rewrite': 'grok-4.5',
  'article-evolve': 'grok-4.5',
  'article-new': 'grok-4.5',
  'pr-review': 'grok-4.5',
  'issue-handle': 'grok-4.5',
  'spore-publish': 'grok-4.5',
  'contributor-thank-you': 'grok-4.5',
  'self-diagnose': 'grok-4.5',
};

const DEFAULT_CLAUDE_MODEL_BY_TYPE: Record<string, string> = {
  'lang-sync-refresh': 'claude-sonnet-4-6',
  'lang-sync-translate': 'claude-sonnet-4-6',
  'data-refresh': 'claude-sonnet-4-6',
  'format-check': 'claude-sonnet-4-6',
  'status-report': 'claude-sonnet-4-6',
  'article-rewrite': 'claude-opus-4-8',
  'article-evolve': 'claude-opus-4-8',
  'article-new': 'claude-opus-4-8',
  'pr-review': 'claude-opus-4-8',
  'issue-handle': 'claude-opus-4-8',
  'spore-publish': 'claude-opus-4-8',
  'contributor-thank-you': 'claude-opus-4-8',
  'self-diagnose': 'claude-opus-4-8',
};

export interface ModelBadge {
  /** short label e.g. "sonnet" / "opus" / "codex" / "qwen" / "4.5" */
  label: string;
  /** engine icon */
  icon: string;
  /** tone for tailwind class */
  tone: 'sonnet' | 'opus' | 'codex' | 'ollama' | 'grok' | 'unknown';
  /** full model id for tooltip */
  full: string;
}

export function modelBadgeForTask(
  type: string,
  inputs: Record<string, unknown> | undefined,
): ModelBadge | null {
  const engine =
    typeof inputs?.engine === 'string'
      ? (inputs.engine as string)
      : DEFAULT_ENGINE;
  const explicitModel =
    typeof inputs?.model === 'string' ? (inputs.model as string) : null;

  if (engine === 'codex') {
    // codex CLI runs on ChatGPT subscription. Model id can be explicit
    // (gpt-5 / o3 / etc) or auto (CLI picks subscription default).
    if (explicitModel) {
      // Strip any vendor prefix for compactness (e.g. 'openai/gpt-5' → 'gpt-5')
      const short = explicitModel.includes('/')
        ? (explicitModel.split('/').pop() ?? explicitModel)
        : explicitModel;
      return {
        label: short,
        icon: '⚙️',
        tone: 'codex',
        full: `codex · ${explicitModel}`,
      };
    }
    return {
      label: 'codex/auto',
      icon: '⚙️',
      tone: 'codex',
      full: 'codex CLI · ChatGPT subscription default (gpt-5 / o3 auto-routed)',
    };
  }
  if (engine === 'ollama') {
    const m = explicitModel ?? 'ollama';
    // qwen3.5:35b-a3b-coding-nvfp4 → "qwen3.5"; gemma3:12b → "gemma3"
    const familySegment = m.split(':')[0] ?? 'ollama';
    const short = familySegment.replace(/[._].*/, ''); // qwen3.5 → qwen3
    return {
      label: short || 'ollama',
      icon: '🦙',
      tone: 'ollama',
      full: `ollama · ${m}`,
    };
  }
  if (engine === 'grok') {
    const m = explicitModel ?? DEFAULT_GROK_MODEL_BY_TYPE[type] ?? 'grok-4.5';
    let short = m;
    if (m.includes('composer')) short = 'composer';
    else if (m.startsWith('grok-')) short = m.slice('grok-'.length);
    return {
      label: short || 'grok',
      icon: '✦',
      tone: 'grok',
      full: `grok · ${m}`,
    };
  }

  // claude
  const model =
    explicitModel ?? DEFAULT_CLAUDE_MODEL_BY_TYPE[type] ?? 'claude-sonnet-4-6';
  if (model.includes('sonnet')) {
    return { label: 'sonnet', icon: '🤖', tone: 'sonnet', full: model };
  }
  if (model.includes('opus')) {
    return { label: 'opus', icon: '🧠', tone: 'opus', full: model };
  }
  if (model.includes('haiku')) {
    return { label: 'haiku', icon: '🪶', tone: 'sonnet', full: model };
  }
  return { label: model, icon: '🤖', tone: 'unknown', full: model };
}

const MODEL_TONE_CLASSES: Record<ModelBadge['tone'], string> = {
  sonnet: 'bg-accent-blue/10 text-accent-blue border border-accent-blue/30',
  opus: 'bg-accent-purple/15 text-accent-purple border border-accent-purple/30',
  codex:
    'bg-accent-green/10 text-accent-green-soft border border-accent-green/30',
  ollama: 'bg-accent-amber/10 text-accent-amber border border-accent-amber/30',
  grok: 'bg-accent-purple/10 text-accent-purple border border-accent-purple/40',
  unknown: 'bg-bg-raised text-text-muted border border-line',
};

export function modelBadgeClass(tone: ModelBadge['tone']): string {
  return MODEL_TONE_CLASSES[tone];
}

/** First metric value as a short label, e.g. {articlesLast7Days:110} → "110 / 7d". */
export function firstMetricSummary(
  metrics: Record<string, unknown> | undefined,
): string {
  if (!metrics) return '';
  const entries = Object.entries(metrics);
  if (entries.length === 0) return '';
  // Prefer the first scalar (number/string) entry. Skip nested objects so
  // organs whose first metric is a map (e.g. languageCoverage = {zh:588,en:407,…})
  // don't render as "[object Object]". If a scalar twin exists later (e.g.
  // translationPct), use that. Otherwise summarise the object inline.
  const scalar = entries.find(
    ([, v]) =>
      typeof v === 'number' || typeof v === 'string' || typeof v === 'boolean',
  );
  const [k, v] = scalar ?? entries[0]!;
  let value: string;
  if (typeof v === 'number') value = v.toLocaleString();
  else if (typeof v === 'string') value = v;
  else if (typeof v === 'boolean') value = v ? 'true' : 'false';
  else if (v && typeof v === 'object') {
    // Inline-summarise small objects: take up to 3 numeric entries.
    const inner = Object.entries(v as Record<string, unknown>)
      .filter(([, iv]) => typeof iv === 'number')
      .slice(0, 3)
      .map(([ik, iv]) => `${ik} ${iv}`)
      .join(' · ');
    value = inner || '—';
  } else {
    value = String(v);
  }
  const label = k
    .replace(/_/g, ' ')
    .replace(/([A-Z])/g, ' $1')
    .toLowerCase()
    .trim();
  return `${value} · ${label}`;
}
