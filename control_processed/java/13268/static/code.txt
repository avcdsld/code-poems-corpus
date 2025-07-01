public static boolean isAuthorizedGrantTypeForService(final String grantType,
                                                          final OAuthRegisteredService registeredService) {
        if (registeredService.getSupportedGrantTypes() != null && !registeredService.getSupportedGrantTypes().isEmpty()) {
            LOGGER.debug("Checking grant type [{}] against supported grant types [{}]", grantType, registeredService.getSupportedGrantTypes());
            return registeredService.getSupportedGrantTypes().stream().anyMatch(s -> s.equalsIgnoreCase(grantType));
        }

        LOGGER.warn("Registered service [{}] does not define any authorized/supported grant types. "
            + "It is STRONGLY recommended that you authorize and assign grant types to the service definition. "
            + "While just a warning for now, this behavior will be enforced by CAS in future versions.", registeredService.getName());
        return true;
    }