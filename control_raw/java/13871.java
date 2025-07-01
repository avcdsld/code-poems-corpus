@Override
    public String encode(final String data, final Optional<RegisteredService> service) {
        try {
            if (service.isPresent()) {
                val registeredService = service.get();
                val publicKey = createRegisteredServicePublicKey(registeredService);
                val result = encodeInternal(data, publicKey, registeredService);
                if (result != null) {
                    return EncodingUtils.encodeBase64(result);
                }
            }
        } catch (final Exception e) {
            LOGGER.warn(e.getMessage(), e);
        }
        return null;
    }