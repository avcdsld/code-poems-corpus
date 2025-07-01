@GetMapping(ENDPOINT_REDIRECT)
    public View redirectToProvider(final HttpServletRequest request, final HttpServletResponse response) {
        var clientName = request.getParameter(Pac4jConstants.DEFAULT_CLIENT_NAME_PARAMETER);
        if (StringUtils.isBlank(clientName)) {
            clientName = (String) request.getAttribute(Pac4jConstants.DEFAULT_CLIENT_NAME_PARAMETER);
        }

        try {
            if (StringUtils.isBlank(clientName)) {
                throw new UnauthorizedServiceException("No client name parameter is provided in the incoming request");
            }
            val client = (IndirectClient<Credentials, CommonProfile>) this.clients.findClient(clientName);
            
            val webContext = new J2EContext(request, response, this.sessionStore);
            val ticket = delegatedClientWebflowManager.store(webContext, client);

            return getResultingView(client, webContext, ticket);
        } catch (final HttpAction e) {
            if (e.getCode() == HttpStatus.UNAUTHORIZED.value()) {
                LOGGER.debug("Authentication request was denied from the provider [{}]", clientName, e);
            } else {
                LOGGER.warn(e.getMessage(), e);
            }
            throw new UnauthorizedServiceException(e.getMessage(), e);
        }
    }