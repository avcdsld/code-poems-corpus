function itemY(legend, itemNumber) {
  var cumSpacingAbove = legend.items
    .slice(itemNumber)
    .reduce(function(prev, item) {
      return prev + (item.spacingAbove || 0);
    }, 0);
  return (
    (legend.items.length - itemNumber - 1) *
      (legend.computedItemHeight + legend.itemSpacing) +
    cumSpacingAbove
  );
}