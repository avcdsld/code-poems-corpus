function reportDelete(context, offset, text) {
  const start = context.getSourceCode().getLocFromIndex(offset);
  const end = context.getSourceCode().getLocFromIndex(offset + text.length);
  const range = [offset, offset + text.length];
  context.report({
    message: 'Delete `{{ code }}`',
    data: { code: showInvisibles(text) },
    loc: { start, end },
    fix(fixer) {
      return fixer.removeRange(range);
    }
  });
}