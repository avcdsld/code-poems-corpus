protected void finalizeEncode(final RequestAbstractType authnRequest,
                                  final BaseSAML2MessageEncoder encoder,
                                  final T samlResponse,
                                  final String relayState) throws Exception {
        encoder.initialize();
        encoder.encode();
    }