import { defineConfig } from 'astro/config';
import solid from '@astrojs/solid-js';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  compressHTML: true,
  integrations: [solid()],
  server: {
    port: 4321,
    host: '127.0.0.1',
  },
  vite: {
    // Tailwind v4: Vite plugin (Astro's documented path) replaces the v3
    // postcss + autoprefixer pipeline. Theme lives in src/styles/global.css.
    plugins: [tailwindcss()],
    server: {
      // Allow LAN if cheyu wants to peek from another device.
      hmr: { overlay: true },
    },
  },
});
