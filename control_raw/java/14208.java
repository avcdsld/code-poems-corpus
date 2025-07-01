protected Authentication authenticateEcpRequest(final Credential credential,
                                                    final Pair<AuthnRequest, MessageContext> authnRequest) {
        val issuer = SamlIdPUtils.getIssuerFromSamlObject(authnRequest.getKey());
        LOGGER.debug("Located issuer [{}] from request prior to authenticating [{}]", issuer, credential.getId());

        val service = getSamlProfileHandlerConfigurationContext().getWebApplicationServiceFactory().createService(issuer);
        LOGGER.debug("Executing authentication request for service [{}] on behalf of credential id [{}]", service, credential.getId());
        val authenticationResult = getSamlProfileHandlerConfigurationContext()
            .getAuthenticationSystemSupport().handleAndFinalizeSingleAuthenticationTransaction(service, credential);
        return authenticationResult.getAuthentication();
    }