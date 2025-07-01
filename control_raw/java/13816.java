public static SPSSODescriptor getSPSsoDescriptor(final EntityDescriptor entityDescriptor) {
        LOGGER.trace("Locating SP SSO descriptor for SAML2 protocol...");
        var spssoDescriptor = entityDescriptor.getSPSSODescriptor(SAMLConstants.SAML20P_NS);
        if (spssoDescriptor == null) {
            LOGGER.trace("Locating SP SSO descriptor for SAML11 protocol...");
            spssoDescriptor = entityDescriptor.getSPSSODescriptor(SAMLConstants.SAML11P_NS);
        }
        if (spssoDescriptor == null) {
            LOGGER.trace("Locating SP SSO descriptor for SAML1 protocol...");
            spssoDescriptor = entityDescriptor.getSPSSODescriptor(SAMLConstants.SAML10P_NS);
        }
        LOGGER.trace("SP SSO descriptor resolved to be [{}]", spssoDescriptor);
        return spssoDescriptor;
    }