import { writeFileSync, mkdirSync } from 'node:fs';
import { icons } from '../../src/icons/taiwan-icons.mjs';
mkdirSync('public/icons', { recursive: true });
writeFileSync(
  'public/icons/taiwan.svg',
  `<svg xmlns="http://www.w3.org/2000/svg">${Object.entries(icons)
    .map(
      ([name, d]) =>
        `<symbol id="${name}" viewBox="0 0 24 24"><path d="${d}"/></symbol>`,
    )
    .join('')}</svg>\n`,
);
