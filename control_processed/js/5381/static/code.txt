function() {
    // Remove current resume listener.
    if (onResume) {
      doc.removeEventListener('resume', onResume, false);
    }
    // Remove visibility change listener.
    if (onVisibilityChange) {
      doc.removeEventListener('visibilitychange', onVisibilityChange, false);
    }
    // Cancel onClose promise if not already cancelled.
    if (onClose) {
      onClose.cancel();
    }
    // Remove Auth event callback.
    if (authEventCallback) {
      self.removeAuthEventListener(authEventCallback);
    }
    // Clear any pending redirect now that it is completed.
    self.pendingRedirect_ = null;
  }