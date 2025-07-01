protected BaseClient<Credentials, CommonProfile> findDelegatedClientByName(final HttpServletRequest request, final String clientName, final Service service) {
        val client = (BaseClient<Credentials, CommonProfile>) this.clients.findClient(clientName);
        LOGGER.debug("Delegated authentication client is [{}] with service [{}}", client, service);
        if (service != null) {
            request.setAttribute(CasProtocolConstants.PARAMETER_SERVICE, service.getId());
            if (!isDelegatedClientAuthorizedForService(client, service)) {
                LOGGER.warn("Delegated client [{}] is not authorized by service [{}]", client, service);
                throw new UnauthorizedServiceException(UnauthorizedServiceException.CODE_UNAUTHZ_SERVICE, StringUtils.EMPTY);
            }
        }
        return client;
    }