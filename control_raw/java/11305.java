@SuppressWarnings("unchecked")
    @CheckForNull
    protected PUB getPublicKey() {
        KeyPair keyPair = getKeyPair();
        return keyPair == null ? null : (PUB) keyPair.getPublic();
    }