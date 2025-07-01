function checkIndexFieldsMatch(indexFields, sortOrder, fields) {
  if (sortOrder) {
    // array has to be a strict subarray of index array. furthermore,
    // the sortOrder fields need to all be represented in the index
    var sortMatches = utils.oneArrayIsStrictSubArrayOfOther(sortOrder, indexFields);
    var selectorMatches = utils.oneArrayIsSubArrayOfOther(fields, indexFields);

    return sortMatches && selectorMatches;
  }

  // all of the user's specified fields still need to be
  // on the left side of the index array, although the order
  // doesn't matter
  return utils.oneSetIsSubArrayOfOther(fields, indexFields);
}