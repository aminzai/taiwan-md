import ts from 'typescript';
// Structural presence, not a claim about linguistic quality.
export function localeKeys(source, locale) {
  const file = ts.createSourceFile(
    'i18n.ts',
    source,
    ts.ScriptTarget.Latest,
    true,
  );
  const keys = new Set();
  function visit(node) {
    if (
      ts.isPropertyAssignment(node) &&
      node.name.getText(file).replace(/^['"]|['"]$/g, '') === locale &&
      ts.isObjectLiteralExpression(node.initializer)
    ) {
      for (const property of node.initializer.properties) {
        if (
          ts.isPropertyAssignment(property) &&
          property.name &&
          !['undefined', 'null', "''", '""'].includes(
            property.initializer.getText(file),
          )
        )
          keys.add(property.name.getText(file).replace(/^['"]|['"]$/g, ''));
      }
    }
    ts.forEachChild(node, visit);
  }
  visit(file);
  return keys;
}
export function keyCoverage(source, locale, baseline = 'zh-TW') {
  const expected = localeKeys(source, baseline),
    present = localeKeys(source, locale);
  const filled = [...expected].filter((key) => present.has(key)).length;
  return {
    ...coverage(filled, expected.size),
    kind: 'explicit-key-presence',
    qualityVerified: false,
  };
}
export function coverage(filled, total) {
  return { filled, total, pct: total ? Math.round((filled / total) * 100) : 0 };
}
