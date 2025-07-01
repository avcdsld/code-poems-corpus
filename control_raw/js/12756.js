function nodeIsUnscopedBinding(item: Node): boolean {
  const value = getValue(item);
  return value && value.unscoped;
}