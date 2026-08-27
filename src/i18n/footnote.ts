/**
 * footnoteUI — i18n strings for the inline footnote source card.
 *
 * The card is the reader-facing half of a citation: hovering (or tapping) a
 * `[n]` marker in the prose pops the matching footnote up next to the cursor,
 * with the source domain, its title, the note text, and one button that opens
 * the source in a new tab. Six strings, no prose.
 *
 * Born 2026-08-28 — 報導者 designer feedback: the academic footnote format
 * reads clearly but nobody actually walks the click → scroll → read → click
 * chain to reach a source.
 * Design: reports/design-footnote-source-cards-2026-08-28.md.
 *
 * `de` is absent on purpose — it is still `enabled: false` in the language
 * registry (OBSERVER-QUEUE #29). `useTranslations` FALLBACK_CHAIN covers any
 * missing key, so a new language degrades to English then Chinese instead of
 * throwing; add its block here when the language is switched on.
 */
export const footnoteUI = {
  en: {
    'footnote.card.source': 'Source',
    'footnote.card.note': 'Note',
    'footnote.card.open': 'Visit source',
    'footnote.card.jump': 'See full note',
    'footnote.card.close': 'Close',
    'footnote.card.aria': 'Footnote {n}',
  },
  ja: {
    'footnote.card.source': '出典',
    'footnote.card.note': '注',
    'footnote.card.open': '出典を開く',
    'footnote.card.jump': '文末の注を見る',
    'footnote.card.close': '閉じる',
    'footnote.card.aria': '脚注 {n}',
  },
  ko: {
    'footnote.card.source': '출처',
    'footnote.card.note': '주석',
    'footnote.card.open': '출처 열기',
    'footnote.card.jump': '본문 끝 각주 보기',
    'footnote.card.close': '닫기',
    'footnote.card.aria': '각주 {n}',
  },
  es: {
    'footnote.card.source': 'Fuente',
    'footnote.card.note': 'Nota',
    'footnote.card.open': 'Abrir fuente',
    'footnote.card.jump': 'Ver la nota completa',
    'footnote.card.close': 'Cerrar',
    'footnote.card.aria': 'Nota {n}',
  },
  fr: {
    'footnote.card.source': 'Source',
    'footnote.card.note': 'Note',
    'footnote.card.open': 'Ouvrir la source',
    'footnote.card.jump': 'Voir la note complète',
    'footnote.card.close': 'Fermer',
    'footnote.card.aria': 'Note {n}',
  },
  vi: {
    'footnote.card.source': 'Nguồn',
    'footnote.card.note': 'Ghi chú',
    'footnote.card.open': 'Mở nguồn',
    'footnote.card.jump': 'Xem chú thích đầy đủ',
    'footnote.card.close': 'Đóng',
    'footnote.card.aria': 'Chú thích {n}',
  },
  id: {
    'footnote.card.source': 'Sumber',
    'footnote.card.note': 'Catatan',
    'footnote.card.open': 'Buka sumber',
    'footnote.card.jump': 'Lihat catatan lengkap',
    'footnote.card.close': 'Tutup',
    'footnote.card.aria': 'Catatan kaki {n}',
  },
  pt: {
    'footnote.card.source': 'Fonte',
    'footnote.card.note': 'Nota',
    'footnote.card.open': 'Abrir a fonte',
    'footnote.card.jump': 'Ver a nota completa',
    'footnote.card.close': 'Fechar',
    'footnote.card.aria': 'Nota {n}',
  },
  hi: {
    'footnote.card.source': 'स्रोत',
    'footnote.card.note': 'टिप्पणी',
    'footnote.card.open': 'स्रोत खोलें',
    'footnote.card.jump': 'पूरी टिप्पणी देखें',
    'footnote.card.close': 'बंद करें',
    'footnote.card.aria': 'फ़ुटनोट {n}',
  },
  ar: {
    'footnote.card.source': 'المصدر',
    'footnote.card.note': 'ملاحظة',
    'footnote.card.open': 'فتح المصدر',
    'footnote.card.jump': 'عرض الحاشية كاملة',
    'footnote.card.close': 'إغلاق',
    'footnote.card.aria': 'حاشية {n}',
  },
  ru: {
    'footnote.card.source': 'Источник',
    'footnote.card.note': 'Примечание',
    'footnote.card.open': 'Открыть источник',
    'footnote.card.jump': 'Смотреть сноску целиком',
    'footnote.card.close': 'Закрыть',
    'footnote.card.aria': 'Сноска {n}',
  },
  'zh-TW': {
    'footnote.card.source': '來源',
    'footnote.card.note': '註解',
    'footnote.card.open': '開啟來源',
    'footnote.card.jump': '看文末腳註',
    'footnote.card.close': '關閉',
    'footnote.card.aria': '腳註 {n}',
  },
} as const;
