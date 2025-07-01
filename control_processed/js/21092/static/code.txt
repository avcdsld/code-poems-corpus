function handleFontLoad (fontFace) {
  _backingStores.forEach(function (backingStore) {
    if (layerContainsFontFace(backingStore.layer, fontFace)) {
      invalidateBackingStore(backingStore.id);
    }
  });
}