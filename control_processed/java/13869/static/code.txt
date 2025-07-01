private static PublicKey createRegisteredServicePublicKey(final RegisteredService registeredService) {
        if (registeredService.getPublicKey() == null) {
            LOGGER.debug("No public key is defined for service [{}]. No encoding will take place.", registeredService);
            return null;
        }
        val publicKey = registeredService.getPublicKey().createInstance();
        if (publicKey == null) {
            LOGGER.debug("No public key instance created for service [{}]. No encoding will take place.", registeredService);
            return null;
        }
        return publicKey;
    }