public static SignatureValidationFilter buildSignatureValidationFilter(final ResourceLoader resourceLoader,
                                                                           final String signatureResourceLocation) {
        try {
            val resource = resourceLoader.getResource(signatureResourceLocation);
            return buildSignatureValidationFilter(resource);
        } catch (final Exception e) {
            LOGGER.debug(e.getMessage(), e);
        }
        return null;
    }