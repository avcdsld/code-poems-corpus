function isArguments(value) {
  return (
    isObjectLike(value) &&
    isArrayLike(value) &&
    hasOwnProperty.call(value, "callee") &&
    !propertyIsEnumerable.call(value, "callee")
  );
}