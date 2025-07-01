public static final PravegaNodeUri encode(final NodeUri uri) {
        Preconditions.checkNotNull(uri, "uri");
        return new PravegaNodeUri(uri.getEndpoint(), uri.getPort());
    }