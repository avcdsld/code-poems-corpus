function getShownDimensions(item, dimensions, fullDimensions) {
  return dimensions.filter(function(dimension, i) {
    return (
      item._suppressedIds.indexOf(dimension.id) === -1 &&
      // note the logic of the next line is repeated in calculateDimensionRequestString
      (fullDimensions[i].values.length > 1 ||
        item.forceShowDimensionIds.indexOf(dimension.id) >= 0) &&
      item.aggregatedDimensionIds.indexOf(dimension.id) === -1
    );
  });
}