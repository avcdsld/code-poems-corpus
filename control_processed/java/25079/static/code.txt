public RuntimeException endQuietly(Throwable ex) {
    try {
      GLOBALS.clear();
      Futures fs = new Futures();
      for (Frame fr : FRAMES.values()) {
        for (Key<Vec> vec : fr.keys()) {
          Integer I = REFCNTS.get(vec);
          int i = (I == null ? 0 : I) - 1;
          if (i > 0) REFCNTS.put(vec, i);
          else {
            REFCNTS.remove(vec);
            vec.remove(fs);
          }
        }
        DKV.remove(fr._key, fs);   // Shallow remove, internal Vecs removed 1-by-1
      }
      fs.blockForPending();
      FRAMES.clear();
      REFCNTS.clear();
    } catch (Exception ex2) {
      Log.warn("Exception " + ex2 + " suppressed while cleaning up Rapids Session after already throwing " + ex);
    }
    return ex instanceof RuntimeException ? (RuntimeException) ex : new RuntimeException(ex);
  }