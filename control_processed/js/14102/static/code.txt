function updateOneLayer(item, currZIndex) {
  if (defined(item.imageryLayer) && defined(item.imageryLayer.setZIndex)) {
    if (item.supportsReordering) {
      item.imageryLayer.setZIndex(currZIndex.reorderable++);
    } else {
      item.imageryLayer.setZIndex(currZIndex.fixed++);
    }
  }
}