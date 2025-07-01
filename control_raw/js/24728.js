function checkOrExpression(range, version) {
  const expressions = range.split(orRegex);

  if (expressions.length > 1) {
    return expressions.some(range => VersionRange.contains(range, version));
  } else {
    range = expressions[0].trim();
    return checkRangeExpression(range, version);
  }
}