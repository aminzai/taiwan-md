/** Analytics labels originate outside the site; never interpret them as HTML. */
export function escapeHtml(value) {
  return String(value ?? '').replace(
    /[&<>"']/g,
    (c) =>
      ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;',
      })[c],
  );
}

export function localAnalyticsPath(value) {
  if (
    typeof value !== 'string' ||
    !value.startsWith('/') ||
    /^[/\\]{2}/.test(value) ||
    /[\\\x00-\x20]/.test(value)
  )
    return '/';
  return value;
}

export function decodePathLabel(value) {
  const path = String(value ?? '').replace(/^\/|\/$/g, '');
  try {
    return decodeURIComponent(path);
  } catch {
    return path;
  }
}
