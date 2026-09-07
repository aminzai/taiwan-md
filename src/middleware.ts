import { defineMiddleware } from 'astro:middleware';
import { renderUiIcons } from './icons/render-ui-icons.mjs';

// Runs during static generation and development; readers receive static SVG.
export const onRequest = defineMiddleware(async (_context, next) => {
  const response = await next();
  if (!response.headers.get('content-type')?.includes('text/html'))
    return response;
  const html = renderUiIcons(await response.text());
  const headers = new Headers(response.headers);
  headers.delete('content-length');
  return new Response(html, {
    status: response.status,
    statusText: response.statusText,
    headers,
  });
});
