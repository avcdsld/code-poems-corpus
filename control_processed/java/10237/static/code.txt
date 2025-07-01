private boolean isFallbackPossible(SSLSocket socket) {
    for (int i = nextModeIndex; i < connectionSpecs.size(); i++) {
      if (connectionSpecs.get(i).isCompatible(socket)) {
        return true;
      }
    }
    return false;
  }