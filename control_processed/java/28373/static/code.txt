@SafeVarargs
    public final Builder retryOn(Class<? extends Exception>... exceptions) {
      for (Class<? extends Exception> exception : exceptions) {
        retriableExceptions.add(checkNotNull(exception));
      }
      return this;
    }