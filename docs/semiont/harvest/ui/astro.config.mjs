import { defineConfig } from 'astro/config';
import solid from '@astrojs/solid-js';

// https://astro.build/config
export default defineConfig({
  compressHTML: true,
  integrations: [solid()],
  server: {
    port: 4321,
    host: '127.0.0.1',
  },
  vite: {
    server: {
      // Allow LAN if cheyu wants to peek from another device.
      hmr: { overlay: true },
    },
  },
});
