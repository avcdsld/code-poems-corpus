function handlePlainCharacter(element, char) {
  const prefix = element[typedPrefixKey] || '';
  element[typedPrefixKey] = prefix + char;
  element.selectItemWithTextPrefix(element[typedPrefixKey]);
  setPrefixTimeout(element);
}