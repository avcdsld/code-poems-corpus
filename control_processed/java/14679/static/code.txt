public static SslContextBuilder forServer(InputStream keyCertChain, InputStream key) {
    return configure(SslContextBuilder.forServer(keyCertChain, key));
  }