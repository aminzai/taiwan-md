/**
 * QuickActionBar — preset task buttons for the captain's bridge.
 *
 * Click → POST /api/tasks with predefined config.
 *
 * Phase 5.1 (2026-04-30) revisions:
 *   - title now read via preset.title() lazy call (fresh timestamp per click)
 *   - per-preset model picker: ⚙️ icon next to model badge → click opens
 *     small popover with engine-eligible model options. Selected model
 *     overrides preset.defaultInputs.model and persists per-preset until
 *     reload.
 *   - notes (if defined on preset) injected into createQuickTask body so
 *     prompt-builder Phase 5.1 task.notes injection picks it up.
 */
import {
  QueryClientProvider,
  useMutation,
  useQueryClient,
} from '@tanstack/solid-query';
import { For, Show, createSignal } from 'solid-js';
import { api } from '~/lib/api';
import { modelBadgeClass, modelBadgeForTask } from '~/lib/format';
import { getQueryClient } from '~/lib/query-client';
import { QUICK_PRESETS, type QuickPreset } from '~/lib/quick-presets';

/**
 * Cross-engine model picker.
 * Phase 5.2 (2026-07-12): default engine = grok (all tiers).
 * Codex is available on every tier; Ollama is simple-tier only.
 */
interface ModelOption {
  /** "engine::model" — model can be empty for engine default */
  value: string;
  label: string;
  engine: 'claude' | 'codex' | 'ollama' | 'grok';
  model: string;
}

const DEFAULT_ENGINE = 'grok';

const ENGINE_GROUPS: {
  engine: 'claude' | 'codex' | 'ollama' | 'grok';
  label: string;
  options: { value: string; label: string }[];
}[] = [
  {
    engine: 'grok',
    label: '✦ Grok (default · all tiers)',
    options: [
      { value: '', label: '(default by type)' },
      { value: 'grok-4.5', label: 'grok-4.5 (heavy)' },
      {
        value: 'grok-composer-2.5-fast',
        label: 'composer 2.5 fast (mechanical)',
      },
    ],
  },
  {
    engine: 'claude',
    label: '🤖 Claude',
    options: [
      { value: '', label: '(default by type)' },
      { value: 'claude-sonnet-4-6', label: 'sonnet 4.6 (cheap)' },
      { value: 'claude-opus-4-8', label: 'opus 4.8 (heavy)' },
      { value: 'claude-haiku-4-5', label: 'haiku 4.5 (faster)' },
    ],
  },
  {
    engine: 'codex',
    label: '⚙️ OpenAI Codex (all tiers)',
    options: [
      { value: '', label: 'auto (~/.codex/config.toml)' },
      { value: 'gpt-5.6-sol', label: 'GPT-5.6 Sol (frontier)' },
      { value: 'gpt-5', label: 'gpt-5' },
      { value: 'gpt-5.5', label: 'gpt-5.5' },
      { value: 'gpt-5-mini', label: 'gpt-5-mini' },
      { value: 'o3', label: 'o3' },
    ],
  },
  {
    engine: 'ollama',
    label: '🦙 Ollama (本機 RTX 3090, $0)',
    options: [
      { value: 'qwen3.5:35b-a3b-coding-nvfp4', label: 'qwen3.5 nvfp4' },
      { value: 'qwen3.6:35b-a3b-coding-nvfp4', label: 'qwen3.6 nvfp4' },
      { value: 'qwen3.6:35b-a3b-coding-mxfp8', label: 'qwen3.6 mxfp8' },
      { value: 'gemma3:12b', label: 'gemma3 12b' },
      { value: 'gpt-oss:20b', label: 'gpt-oss 20b' },
    ],
  },
];

/**
 * Task types that accept non-peer engine override (Ollama).
 */
const ENGINE_OVERRIDE_OK = new Set([
  'data-refresh',
  'format-check',
  'status-report',
  'lang-sync-refresh',
  'lang-sync-translate',
]);

const PEER_ENGINES = new Set(['claude', 'grok', 'codex']);

/** Encode (engine, model) → option value. */
function encodeOpt(engine: string, model: string): string {
  return `${engine}::${model}`;
}

/** Decode option value → (engine, model). */
function decodeOpt(value: string): { engine: string; model: string } {
  const idx = value.indexOf('::');
  if (idx < 0) return { engine: DEFAULT_ENGINE, model: value };
  return {
    engine: value.slice(0, idx),
    model: value.slice(idx + 2),
  };
}

/**
 * Infer current engine from preset.defaultInputs.engine, default grok.
 */
function engineFor(p: QuickPreset): string {
  const e = p.defaultInputs?.engine;
  return typeof e === 'string' ? e : DEFAULT_ENGINE;
}

function Inner() {
  const qc = useQueryClient();
  const [busy, setBusy] = createSignal<string | null>(null);
  const [flash, setFlash] = createSignal<{
    type: 'ok' | 'err';
    msg: string;
  } | null>(null);
  // Per-preset model overrides (preset.id → model id). Empty string = use default.
  const [modelOverrides, setModelOverrides] = createSignal<
    Record<string, string>
  >({});
  // Which preset's picker is open (null = none).
  const [pickerOpen, setPickerOpen] = createSignal<string | null>(null);

  const fire = useMutation(() => ({
    mutationFn: async (preset: QuickPreset) => {
      const overrideValue = modelOverrides()[preset.id];
      // Phase 5.2: always default engine=grok unless preset/override says otherwise
      const inputs: Record<string, unknown> = {
        engine: DEFAULT_ENGINE,
        ...(preset.defaultInputs ?? {}),
      };
      if (overrideValue && !preset.lockModel) {
        const { engine, model } = decodeOpt(overrideValue);
        // Peer agents always OK; only Ollama is limited to simple tasks.
        if (
          PEER_ENGINES.has(engine) ||
          ENGINE_OVERRIDE_OK.has(preset.taskType)
        ) {
          inputs.engine = engine;
        } else {
          inputs.engine = DEFAULT_ENGINE;
        }
        if (model) inputs.model = model;
        else delete inputs.model;
      }
      const task = await api.createQuickTask({
        type: preset.taskType,
        boot_profile: preset.bootProfile,
        priority: preset.priority,
        title: preset.title(), // lazy — fresh timestamp per click
        ...(preset.notes ? { notes: preset.notes } : {}),
        inputs,
      });
      if (preset.autoSpawn) {
        await api.spawnTask(task.id);
      }
      return { task, spawned: preset.autoSpawn === true };
    },
    onSuccess: (result, preset) => {
      setFlash({
        type: 'ok',
        msg: result.spawned
          ? `🚀 Pipeline running: ${preset.label}`
          : `✅ Task created: ${preset.label}`,
      });
      void qc.invalidateQueries({ queryKey: ['tasks'] });
      setTimeout(() => setFlash(null), 3000);
    },
    onError: (err) => {
      setFlash({ type: 'err', msg: `❌ ${(err as Error).message}` });
      setTimeout(() => setFlash(null), 5000);
    },
    onSettled: () => setBusy(null),
  }));

  const setModel = (presetId: string, model: string): void => {
    setModelOverrides({ ...modelOverrides(), [presetId]: model });
    setPickerOpen(null);
  };

  return (
    <div class="space-y-3">
      <Show when={flash()}>
        <div
          class={`text-xs rounded px-3 py-2 ${
            flash()!.type === 'ok'
              ? 'bg-accent-green/15 text-accent-green-soft border border-accent-green/40'
              : 'bg-accent-red/15 text-accent-red border border-accent-red/40'
          }`}
        >
          {flash()!.msg}
        </div>
      </Show>
      <div class="grid grid-cols-2 gap-2">
        <For each={QUICK_PRESETS}>
          {(p) => {
            // Effective inputs combining preset + override for badge derivation
            const effectiveInputs = (): Record<string, unknown> => {
              const ovr = modelOverrides()[p.id];
              const out: Record<string, unknown> = {
                engine: DEFAULT_ENGINE,
                ...(p.defaultInputs ?? {}),
              };
              if (!ovr) return out;
              const { engine, model } = decodeOpt(ovr);
              out.engine = engine;
              if (model) out.model = model;
              else delete out.model;
              return out;
            };
            const badge = (): ReturnType<typeof modelBadgeForTask> =>
              modelBadgeForTask(p.taskType, effectiveInputs());
            const overrideAllowed = ENGINE_OVERRIDE_OK.has(p.taskType);
            const currentValue = (): string => {
              const ovr = modelOverrides()[p.id];
              if (ovr) return ovr;
              const e = engineFor(p);
              const m =
                typeof p.defaultInputs?.model === 'string'
                  ? (p.defaultInputs.model as string)
                  : '';
              return encodeOpt(e, m);
            };

            return (
              <div
                class="relative text-left text-sm px-3 py-2 rounded-md border border-line
                     bg-bg-raised hover:bg-bg-input hover:border-accent-green/40
                     transition-colors"
              >
                <button
                  type="button"
                  title={p.description}
                  disabled={busy() === p.id}
                  onClick={() => {
                    setBusy(p.id);
                    fire.mutate(p);
                  }}
                  class="block w-full text-left disabled:opacity-60"
                >
                  <div class="flex items-center gap-2">
                    <span class="text-base shrink-0">{p.emoji}</span>
                    <span class="font-medium text-text-primary truncate flex-1">
                      {p.label}
                    </span>
                  </div>
                  <div class="flex items-center gap-1.5 mt-0.5 text-xs text-text-muted">
                    <span class="shrink-0">{p.priority}</span>
                    <span class="shrink-0">·</span>
                    <span class="truncate flex-1">{p.taskType}</span>
                  </div>
                </button>
                {/* Model picker — clickable badge that opens dropdown */}
                <div class="absolute top-1 right-1 flex items-center gap-1">
                  <Show when={badge()}>
                    {(b) =>
                      p.lockModel ? (
                        <span
                          class={`text-[10px] px-1 py-px rounded border leading-tight ${modelBadgeClass(b().tone)}`}
                          title={`${b().full} — locked by strict pipeline contract`}
                        >
                          🔒{b().label}
                        </span>
                      ) : (
                        <button
                          type="button"
                          class={`text-[10px] px-1 py-px rounded border leading-tight cursor-pointer hover:opacity-80 ${modelBadgeClass(b().tone)}`}
                          title={`${b().full} — click to change model`}
                          onClick={(e) => {
                            e.stopPropagation();
                            setPickerOpen(pickerOpen() === p.id ? null : p.id);
                          }}
                        >
                          {b().icon}
                          {b().label}
                          <span class="ml-0.5 opacity-70">▾</span>
                        </button>
                      )
                    }
                  </Show>
                </div>
                <Show when={pickerOpen() === p.id}>
                  <div
                    class="absolute top-7 right-1 z-10 min-w-[220px] py-1
                           border border-line rounded-md bg-bg-raised shadow-lg
                           text-xs max-h-[400px] overflow-y-auto"
                  >
                    <Show when={!overrideAllowed}>
                      <div class="px-2 py-1 text-[10px] text-accent-amber border-b border-line/40">
                        ⚠️ heavy task — peer engines only (Ollama ignored)
                      </div>
                    </Show>
                    <For each={ENGINE_GROUPS}>
                      {(group) => {
                        const isHeavyClause =
                          !overrideAllowed && !PEER_ENGINES.has(group.engine);
                        return (
                          <div>
                            <div class="px-2 py-1 text-text-muted text-[10px] uppercase tracking-wide bg-bg-input/30">
                              {group.label}
                            </div>
                            <For each={group.options}>
                              {(opt) => {
                                const optValue = encodeOpt(
                                  group.engine,
                                  opt.value,
                                );
                                const isSelected = currentValue() === optValue;
                                return (
                                  <button
                                    type="button"
                                    class={`block w-full text-left px-3 py-1 hover:bg-bg-input ${
                                      isSelected
                                        ? 'text-accent-green-soft font-medium'
                                        : isHeavyClause
                                          ? 'text-text-muted opacity-50 cursor-not-allowed'
                                          : 'text-text-primary'
                                    }`}
                                    disabled={isHeavyClause}
                                    onClick={(e) => {
                                      e.stopPropagation();
                                      if (isHeavyClause) return;
                                      setModel(p.id, optValue);
                                    }}
                                  >
                                    {isSelected ? '✓ ' : '  '}
                                    {opt.label}
                                  </button>
                                );
                              }}
                            </For>
                          </div>
                        );
                      }}
                    </For>
                  </div>
                </Show>
              </div>
            );
          }}
        </For>
      </div>
      <Show when={pickerOpen()}>
        {/* Click outside to close picker */}
        <div
          class="fixed inset-0 z-0"
          onClick={() => setPickerOpen(null)}
          aria-hidden="true"
        />
      </Show>
    </div>
  );
}

export default function QuickActionBar() {
  return (
    <QueryClientProvider client={getQueryClient()}>
      <Inner />
    </QueryClientProvider>
  );
}
