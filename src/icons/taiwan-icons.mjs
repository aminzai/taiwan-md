/** Taiwan.md Island Lines. Original 24-unit editorial glyphs, 1.5-unit stroke.
 * Open paths echo contour lines; offset circles echo coast/island relationships.
 * Paths contain no user data. Sprite and inline renderers share this registry.
 */
export const icons = {
  headphones:
    'M3 14v-3a9 9 0 0 1 18 0v3 M3 12h3v8H4a2 2 0 0 1-2-2v-4a2 2 0 0 1 1-2Z M21 12h-3v8h2a2 2 0 0 0 2-2v-4a2 2 0 0 0-1-2Z',
  question:
    'M9 8a3 3 0 1 1 5 2c-2 1-2 2-2 3 M12 17h.01 M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Z',
  door: 'M5 21V3h14v18 M9 21V6l7-3v18 M12 12h.01 M3 21h18',
  dice: 'M5 3h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2Z M7 7h.01 M17 7h.01 M12 12h.01 M7 17h.01 M17 17h.01',
  balance: 'M12 3v18 M6 21h12 M4 7h16 M5 7 2 14h6L5 7Z M19 7l-3 7h6l-3-7Z',
  lantern:
    'M9 3h6 M12 1v2 M7 6h10c5 4 5 8 0 12H7c-5-4-5-8 0-12Z M9 6c-2 4-2 8 0 12 M15 6c2 4 2 8 0 12 M12 18v5',
  brain:
    'M12 5c-3-5-8-1-7 3-4 2-3 7 0 8-1 5 5 7 7 3 2 4 8 2 7-3 3-1 4-6 0-8 1-4-4-8-7-3v14 M5 8l3 2 M19 8l-3 2 M5 16l3-2 M19 16l-3-2',
  antenna:
    'M12 10v11 M8 21h8 M8 7a6 6 0 0 0 0 8 M16 7a6 6 0 0 1 0 8 M5 4a10 10 0 0 0 0 14 M19 4a10 10 0 0 1 0 14 M12 10h.01',
  plug: 'M8 3v5 M16 3v5 M5 8h14 M7 8v5a5 5 0 0 0 10 0V8 M12 18v4',
  code: 'm8 6-6 6 6 6 M16 6l6 6-6 6 M14 3l-4 18',
  flame:
    'M13 2c2 7-4 6-2 11 2-2 4-3 5-5 6 7 4 13-3 14C4 23 1 16 6 10c0 4 3 5 3 2-1-4 2-6 4-10Z',
  bone: 'M7 3c-3-2-6 1-4 4-1 3 2 5 4 3l7 7c-2 2 0 5 3 4 3 2 6-1 4-4 1-3-2-5-4-3l-7-7c2-2 0-5-3-4Z',
  lungs:
    'M12 3v8 M12 8l-4 4 M12 8l4 4 M8 6C3 9 1 17 3 20c1 2 5 0 6-2V9 M16 6c5 3 7 11 5 14-1 2-5 0-6-2V9',
  petri:
    'M3 10c0-4 18-4 18 0s-18 4-18 0v6c0 5 18 5 18 0v-6 M8 10h.01 M15 9h.01 M12 16h.01',

  island:
    'M15 3c-3 2-3 5-5 7s-3 6-3 9c2 3 5-1 6-3s1-4 3-6 2-5-1-7Z M4 16h1 M19 7h1',
  mountain: 'M2 19 9 6l4 7 3-5 6 11H2Z M6 12l3 2 3-2 M16 8l2 5',
  map: 'M3 5 9 3l6 3 6-2v15l-6 2-6-3-6 2V5Z M9 3v15 M15 6v15',
  book: 'M12 6C9 3 5 3 3 4v15c3-1 6-1 9 1 3-2 6-2 9-1V4c-3-1-6-1-9 2v14 M6 8h3 M15 8h3',
  archive:
    'M6 3h13v16a2 2 0 0 1-2 2H6a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3Z M6 3v18 M9 7h7 M9 11h7 M9 15h4',
  art: 'M12 3a9 9 0 1 0 0 18h1c2 0 3-2 1-4s0-3 2-3h2c5 0 3-11-6-11Z M7 8h.01 M12 6h.01 M17 8h.01 M6 13h.01',
  bowl: 'M3 12h18c-1 5-4 7-9 7s-8-2-9-7Z M8 21h8 M8 3c-3 3 3 3 0 6 M13 3c-3 3 3 3 0 6 M17 7l4-5',
  music:
    'M9 17V5l11-2v12 M9 9l11-2 M9 17c0 4-6 5-6 2s6-4 6-2Z M20 15c0 4-6 5-6 2s6-4 6-2Z',
  network:
    'M7 7l10 10 M7 17 17 7 M7 5h10 M5 7v10 M19 7v10 M7 19h10 M7 5a2 2 0 1 0-4 0 2 2 0 0 0 4 0 M21 5a2 2 0 1 0-4 0 2 2 0 0 0 4 0 M7 19a2 2 0 1 0-4 0 2 2 0 0 0 4 0 M21 19a2 2 0 1 0-4 0 2 2 0 0 0 4 0',
  chip: 'M6 6h12v12H6V6Z M9 9h6v6H9V9Z M9 2v4 M15 2v4 M9 18v4 M15 18v4 M2 9h4 M2 15h4 M18 9h4 M18 15h4',
  leaf: 'M20 3C10 2 3 7 5 15c6 8 16 0 15-12Z M3 21 15 9 M8 16l-1-5 M11 13h5',
  person: 'M16 7a4 4 0 1 0-8 0 4 4 0 0 0 8 0 M4 21v-2c0-4 4-6 8-6s8 2 8 6v2',
  community:
    'M14 6a3 3 0 1 0-6 0 3 3 0 0 0 6 0 M3 21v-3c0-4 3-6 8-6s8 2 8 6v3 M18 4c4 0 4 6 0 6 M21 13c2 1 2 4 2 6',
  chart: 'M3 3v18h18 M7 16v-4 M12 16V8 M17 16V5 M5 8l5-3 4 1 6-4',
  home: 'M2 11 12 3l10 8 M5 10v11h14V10 M10 21v-7h4v7',
  civic: 'M3 9 12 3l9 6H3Z M5 12v6 M10 12v6 M15 12v6 M20 12v6 M2 21h20',
  shield: 'M12 3 3 6v6c0 5 5 8 9 10 4-2 9-5 9-10V6l-9-3Z M8 12l3 3 5-6',
  spark: 'M12 2 9 9 2 12l7 3 3 7 3-7 7-3-7-3-3-7Z M19 3v3 M18 4h3',
  search: 'M17 10a7 7 0 1 0-14 0 7 7 0 0 0 14 0 M15 15l7 7',
  arrow: 'M3 12h17 M14 5l7 7-7 7',
  check: 'M4 12l5 5L20 5',
  close: 'M5 5l14 14 M5 19 19 5',
  alert: 'M12 3 2 21h20L12 3Z M12 9v5 M12 18h.01',
  clock: 'M21 12a9 9 0 1 0-18 0 9 9 0 0 0 18 0 M12 6v6l4 2',
  language:
    'M3 5h11 M8 2v3 M5 5c0 6 4 9 8 11 M12 5c-1 5-4 9-9 11 M13 21l4-10 4 10 M15 17h4',
  comment: 'M4 3h16v14H9l-5 4V3Z M8 7h8 M8 11h5',
  link: 'M10 7l3-3c5-4 10 1 6 6l-3 3 M14 17l-3 3c-5 4-10-1-6-6l3-3 M8 16l8-8',
  heart: 'M12 21 3 12C-2 4 7-1 12 6c5-7 14-2 9 6l-9 9Z',
  camera: 'M3 7h4l2-3h6l2 3h4v14H3V7Z M16 13a4 4 0 1 0-8 0 4 4 0 0 0 8 0',
  train:
    'M6 3h12v14H6V3Z M6 10h12 M9 3v7 M5 22l4-5 M19 22l-4-5 M9 14h.01 M15 14h.01',
  city: 'M3 21V9h6v12 M9 21V3h8v18 M17 21V12h4v9 M12 7h2 M12 11h2 M12 15h2 M2 21h20',
  wave: 'M2 9c4-5 6 5 10 0s6 5 10 0 M2 15c4-5 6 5 10 0s6 5 10 0 M2 21c4-5 6 5 10 0s6 5 10 0',
  mail: 'M3 5h18v14H3V5Z M3 6l9 7 9-7',
  globe:
    'M21 12a9 9 0 1 0-18 0 9 9 0 0 0 18 0 M3 12h18 M12 3c-5 5-5 13 0 18 5-5 5-13 0-18Z',
  pin: 'M18 9c0 5-6 12-6 12S6 14 6 9a6 6 0 0 1 12 0Z M14 9a2 2 0 1 0-4 0 2 2 0 0 0 4 0',
  sun: 'M16 12a4 4 0 1 0-8 0 4 4 0 0 0 8 0 M12 1v3 M12 20v3 M1 12h3 M20 12h3 M4 4l2 2 M18 18l2 2 M4 20l2-2 M18 6l2-2',
  moon: 'M20 16A9 9 0 0 1 8 4a9 9 0 1 0 12 12Z',
  tool: 'M14 3c-3 1-4 4-3 7l-8 8 3 3 8-8c4 1 7-2 7-6l-4 3-3-3 3-4h-3Z',
  eye: 'M2 12c5-9 15-9 20 0-5 9-15 9-20 0Z M15 12a3 3 0 1 0-6 0 3 3 0 0 0 6 0',
  flag: 'M5 22V3c5-3 9 3 15 0v11c-6 3-10-3-15 0',
  trophy:
    'M8 3h8v8c0 5-8 5-8 0V3Z M8 5H3v4c0 3 3 4 5 3 M16 5h5v4c0 3-3 4-5 3 M12 15v6 M7 21h10',
  seed: 'M12 22V11 M12 13C4 14 2 8 3 3c7 0 10 4 9 10Z M12 17c-1-7 4-11 10-10 0 6-3 10-10 10Z',
};
// Migration aliases preserve semantic meaning; flags and the 🧬 signature stay text.
export const emojiIcons = Object.fromEntries(
  Object.entries({
    headphones: ['🎧'],
    question: ['❓'],
    door: ['🚪'],
    dice: ['🎲'],
    balance: ['⚖️', '🆚'],
    lantern: ['🏮'],
    brain: ['🧠'],
    antenna: ['📡'],
    plug: ['🔌'],
    code: ['🐙'],
    flame: ['🔥'],
    bone: ['🦴'],
    lungs: ['🫁'],
    petri: ['🧫'],
    island: ['🏝️'],
    mountain: ['🏔️', '⛰️', '🌋'],
    map: ['🗺️', '🧭'],
    book: ['📰', '📚', '📖', '📘', '📗', '📙'],
    archive: ['📁', '🧾', '📂', '📜', '🗂️', '📋', '📝', '📄'],
    art: ['📐', '✏️', '✏', '🖊️', '🎨', '🖌️', '🎭'],
    bowl: ['🍜', '🍲', '🍚', '🍱', '🍴', '🍽️', '🧋', '🍵', '☕'],
    music: ['🎵', '🎶', '🎸', '🎤', '🥁', '🎷'],
    network: ['🔁', '🕸️', '🔗'],
    chip: ['🤖', '💻', '🖥️', '⚙️', '🔬'],
    leaf: ['♻️', '♻', '🌿', '🌳', '🌲', '🍃', '🌾'],
    person: ['🆕', '👤', '🧑', '👨‍🎨'],
    community: ['✋', '👥', '🤝'],
    chart: ['🪙', '📊', '📈', '📉', '💰', '💵'],
    home: ['🏠', '🏡'],
    civic: ['🏛️', '🗳️'],
    shield: ['🛡️', '🔒', '🔐'],
    spark: ['🎉', '⚡', '✨', '🌟', '⭐', '💡', '🎯'],
    search: ['🔍', '🔎'],
    arrow: ['➡️', '➜', '🚀'],
    check: ['✅', '✔️', '☑️', '🟢'],
    close: ['❌', '✖️', '🔴'],
    alert: ['🔔', '⚠️', '🚨', '🟡', '❗'],
    clock: ['⏱️', '⏰', '⏳', '🕐', '📅', '🗓️'],
    language: ['🔤'],
    comment: ['💬', '🗣️', '📢', '📣'],
    heart: ['💓', '🩺', '💖', '🫀', '❤️', '💚', '🧡', '💙', '💜', '♥️'],
    camera: ['📸', '📷', '🎬', '🎥'],
    train: ['🚂', '🚆', '🚇', '🚄', '🚅', '🚃'],
    city: ['🏙️', '🏢', '🏘️'],
    wave: ['☁️', '☁', '🌊', '💧'],
    mail: ['📬', '✉️', '📧', '📮', '📨'],
    globe: ['🌍', '🌎', '🌏', '🌐'],
    pin: ['📍', '📌'],
    sun: ['☀️', '🌞'],
    moon: ['🌙', '🌛'],
    tool: ['🔧', '🛠️', '🔨', '🧰'],
    eye: ['👁️'],
    flag: ['🚩', '🏁'],
    trophy: ['🥈', '🥉', '🏆', '🥇', '🎖️'],
    seed: ['🌱', '🌸', '🌺', '🌻'],
  }).flatMap(([name, emojis]) => emojis.map((emoji) => [emoji, name])),
);
export function iconSvg(name, label = '') {
  if (!(name in icons)) throw new Error(`Unknown Taiwan.md icon: ${name}`);
  const safeLabel = label.replace(
    /[&<>"']/g,
    (c) =>
      ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[
        c
      ],
  );
  return `<svg class="twmd-icon" viewBox="0 0 24 24" width="1em" height="1em" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" focusable="false" ${label ? `role="img" aria-label="${safeLabel}"` : 'aria-hidden="true"'}><use href="/icons/taiwan.svg#${name}"/></svg>`;
}
