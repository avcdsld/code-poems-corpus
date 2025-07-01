function _parseLeafToken(token) {
  const [, name, remainder] = token.match(LEAF_REGEX);

  return {
    name: name.toLowerCase(),
    params: _parseParams(remainder),
  };
}