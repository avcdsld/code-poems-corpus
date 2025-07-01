@SneakyThrows
    public static OidcClientRegistrationResponse getClientRegistrationResponse(final OidcRegisteredService registeredService,
                                                                               final String serverPrefix) {
        val clientResponse = new OidcClientRegistrationResponse();
        clientResponse.setApplicationType(registeredService.getApplicationType());
        clientResponse.setClientId(registeredService.getClientId());
        clientResponse.setClientSecret(registeredService.getClientSecret());
        clientResponse.setSubjectType(registeredService.getSubjectType());
        clientResponse.setTokenEndpointAuthMethod(registeredService.getTokenEndpointAuthenticationMethod());
        clientResponse.setClientName(registeredService.getName());
        clientResponse.setRedirectUris(CollectionUtils.wrap(registeredService.getServiceId()));
        clientResponse.setContacts(
            registeredService.getContacts()
                .stream()
                .map(RegisteredServiceContact::getName)
                .filter(StringUtils::isNotBlank)
                .collect(Collectors.toList())
        );
        clientResponse.setGrantTypes(
            Arrays.stream(OAuth20GrantTypes.values())
                .map(type -> type.getType().toLowerCase())
                .collect(Collectors.toList()));

        clientResponse.setResponseTypes(
            Arrays.stream(OAuth20ResponseTypes.values())
                .map(type -> type.getType().toLowerCase())
                .collect(Collectors.toList()));

        val validator = new SimpleUrlValidatorFactoryBean(false).getObject();
        if (Objects.requireNonNull(validator).isValid(registeredService.getJwks())) {
            clientResponse.setJwksUri(registeredService.getJwks());
        } else {
            val jwks = new JsonWebKeySet(registeredService.getJwks());
            clientResponse.setJwks(jwks.toJson());
        }
        clientResponse.setLogo(registeredService.getLogo());
        clientResponse.setPolicyUri(registeredService.getInformationUrl());
        clientResponse.setTermsOfUseUri(registeredService.getPrivacyUrl());
        clientResponse.setRedirectUris(CollectionUtils.wrapList(registeredService.getServiceId()));
        val clientConfigUri = getClientConfigurationUri(registeredService, serverPrefix);
        clientResponse.setRegistrationClientUri(clientConfigUri);
        return clientResponse;
    }