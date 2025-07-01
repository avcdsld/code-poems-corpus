public synchronized void closeDriver() {
    if (camera != null) {
      camera.getCamera().release();
      camera = null;
      // Make sure to clear these each time we close the camera, so that any scanning rect
      // requested by intent is forgotten.
      framingRect = null;
      framingRectInPreview = null;
    }
  }