@ExperimentalApi("https://github.com/grpc/grpc-java/issues/1784")
  @CanIgnoreReturnValue
  public static SslContextBuilder configure(SslContextBuilder builder, SslProvider provider) {
    switch (provider) {
      case JDK:
      {
        Provider jdkProvider = findJdkProvider();
        if (jdkProvider == null) {
          throw new IllegalArgumentException(
              "Could not find Jetty NPN/ALPN or Conscrypt as installed JDK providers");
        }
        return configure(builder, jdkProvider);
      }
      case OPENSSL:
      {
        ApplicationProtocolConfig apc;
        if (OpenSsl.isAlpnSupported()) {
          apc = NPN_AND_ALPN;
        } else {
          apc = NPN;
        }
        return builder
            .sslProvider(SslProvider.OPENSSL)
            .ciphers(Http2SecurityUtil.CIPHERS, SupportedCipherSuiteFilter.INSTANCE)
            .applicationProtocolConfig(apc);
      }
      default:
        throw new IllegalArgumentException("Unsupported provider: " + provider);
    }
  }