/**
 * MJS mirror of src/config/languages.ts.
 *
 * Used by Node-direct scripts and Astro config:
 *  - astro.config.mjs
 *  - scripts/core/generate-dashboard-data.js
 *  - scripts/core/build-search-index.mjs (when refactored)
 *
 * For TypeScript files, import from `./languages` (resolver picks .ts).
 *
 * ⚠️ MUST stay in sync with languages.ts.
 *    `bash scripts/tools/check-language-registry-sync.sh` enforces this.
 *
 * Why two files: Vite SSR prerender chunks bundle the .mjs file but break
 * any filesystem-relative paths (so we can't read JSON via readFileSync).
 * Inlining the data in both files is the most reliable approach.
 */

export const LANGUAGES = [
  {
    code: 'zh-TW',
    displayName: '中文',
    hreflang: 'zh-Hant',
    isDefault: true,
    enabled: true,
  },
  {
    code: 'en',
    displayName: 'English',
    hreflang: 'en',
    enabled: true,
  },
  {
    code: 'ja',
    displayName: '日本語',
    hreflang: 'ja',
    enabled: true,
  },
  {
    code: 'ko',
    displayName: '한국어',
    hreflang: 'ko',
    enabled: true,
  },
  {
    code: 'es',
    displayName: 'Español',
    hreflang: 'es',
    enabled: true,
    notes:
      '2026-04-25 enabled. 36 articles from knowledge/es/. UI bundle wired through src/i18n/ui.ts on 2026-05-02.',
  },
  {
    code: 'fr',
    displayName: 'Français',
    hreflang: 'fr',
    enabled: true,
    notes:
      '2026-04-24 β3 enabled. 484 articles from ceruleanstring + community. UI bundle wired through src/i18n/ui.ts on 2026-05-02.',
  },
  {
    code: 'vi',
    displayName: 'Tiếng Việt',
    hreflang: 'vi',
    enabled: true,
    notes:
      '2026-07-18 selected (disabled scaffold). Highest unserved SC demand (7,994 imp / 0.5% CTR) + largest new-immigrant community in Taiwan. 2026-07-19 enabled (birth battle). Report: reports/language-birth-2026-07-18.md',
  },
  {
    code: 'id',
    displayName: 'Bahasa Indonesia',
    hreflang: 'id',
    enabled: true,
    notes:
      '2026-07-18 selected (disabled scaffold). SC 5,521 imp / 0.3% CTR + largest migrant-worker community in Taiwan. 2026-07-19 enabled (birth battle). Report: reports/language-birth-2026-07-18.md',
  },
  {
    code: 'pt',
    displayName: 'Português',
    hreflang: 'pt',
    enabled: true,
    notes:
      '2026-07-18 selected (disabled scaffold). Only gap confirmed by all three sources (SC 6,659 imp / 0.1% CTR + CF #6 + GA). Reuses es LatAm playbook. 2026-07-19 enabled (birth battle). Report: reports/language-birth-2026-07-18.md',
  },
  {
    code: 'hi',
    displayName: 'हिन्दी',
    hreflang: 'hi',
    enabled: true,
    notes:
      '2026-07-18 selected (disabled scaffold). Largest unserved language (609M speakers, Ethnologue 2025 #3). 2026-07-19 enabled (birth battle). Report: reports/language-birth-2026-07-18.md',
  },
  {
    code: 'ar',
    displayName: 'العربية',
    hreflang: 'ar',
    enabled: true,
    // dir: 'rtl' — mirrors LanguageEntry.dir in languages.ts. First RTL language.
    // Wired into Layout.astro's <html lang dir> block since 2026-07-26; the CSS
    // side (physical → logical properties across the localized reader surface)
    // landed with scripts/tools/check-rtl-safe-css.sh guarding the regression.
    dir: 'rtl',
    notes:
      '2026-07-25 creator-directed birth (哲宇 directive, folded into 100% sync goal). Sovereignty rationale: 400M+ speakers whose Taiwan coverage flows mostly through PRC-funded Arabic outlets. Report: reports/language-birth-2026-07-25.md',
  },
  {
    code: 'ru',
    displayName: 'Русский',
    hreflang: 'ru',
    enabled: true,
    notes:
      '2026-07-25 creator-directed birth (哲宇 directive, folded into 100% sync goal). Sovereignty rationale: Russian-language information sphere about Taiwan is heavily penetrated by PRC-Russia aligned narratives. Report: reports/language-birth-2026-07-25.md',
  },
  {
    code: 'de',
    displayName: 'Deutsch',
    hreflang: 'de',
    enabled: true,
    notes:
      '2026-08-19 scaffold (tboydar de-translations-batch2). 84 de articles in knowledge/de/ (contributor PRs merged). ' +
      '2026-09-05 Stage 2-4 + 6-prep per OBSERVER-QUEUE #29 (哲宇 拍板): model calibration (codex + ollama qwen3.8:27b, 4-article set incl. 戒嚴時期) + ' +
      'ratio band recalibrated from 84-article sample (p5/p95) + QA gate wiring (cjk-leak-check/geo-fidelity-check German markers) + ' +
      'src/i18n/ 18 bundles + src/pages/de/ route scaffold + TRANSLATION-de.md. QA: reports/babel/de-birth-qa-2026-09-05.md. ' +
      '2026-09-05 Stage 5 flip (enabled: true) by 主 session fortnight-review after 13 de Hubs + data/budget/i18n/de.json + skipLink de landed (OBSERVER-QUEUE #29 哲宇拍板 A).',
  },
];

export const ENABLED_LANGUAGE_CODES = LANGUAGES.filter((l) => l.enabled).map(
  (l) => l.code,
);

export const ALL_LANGUAGE_CODES = LANGUAGES.map((l) => l.code);

export const DEFAULT_LANGUAGE = LANGUAGES.find((l) => l.isDefault);

export const LANGUAGE_DISPLAY_NAMES = Object.fromEntries(
  LANGUAGES.map((l) => [l.code, l.displayName]),
);

export function getLanguage(code) {
  return LANGUAGES.find((l) => l.code === code);
}
