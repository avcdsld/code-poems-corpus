protected JsonWebKey getJsonWebKeyForEncryption(final OidcRegisteredService svc) {
        LOGGER.debug("Service [{}] is set to encrypt tokens", svc);
        val jwks = this.serviceJsonWebKeystoreCache.get(svc);
        if (Objects.requireNonNull(jwks).isEmpty()) {
            throw new IllegalArgumentException("Service " + svc.getServiceId()
                + " with client id " + svc.getClientId()
                + " is configured to encrypt tokens, yet no JSON web key is available");
        }
        val jsonWebKey = jwks.get();
        LOGGER.debug("Found JSON web key to encrypt the token: [{}]", jsonWebKey);
        if (jsonWebKey.getPublicKey() == null) {
            throw new IllegalArgumentException("JSON web key used to sign the token has no associated public key");
        }
        return jsonWebKey;
    }