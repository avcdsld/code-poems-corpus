@Deprecated
    public static SslContext newClientContext(
            File certChainFile, TrustManagerFactory trustManagerFactory,
            Iterable<String> ciphers, Iterable<String> nextProtocols,
            long sessionCacheSize, long sessionTimeout) throws SSLException {
        return newClientContext(
                null, certChainFile, trustManagerFactory,
                ciphers, nextProtocols, sessionCacheSize, sessionTimeout);
    }