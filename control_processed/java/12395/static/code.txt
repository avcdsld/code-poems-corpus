public void setFontAssetDelegate(
      @SuppressWarnings("NullableProblems") FontAssetDelegate assetDelegate) {
    this.fontAssetDelegate = assetDelegate;
    if (fontAssetManager != null) {
      fontAssetManager.setDelegate(assetDelegate);
    }
  }