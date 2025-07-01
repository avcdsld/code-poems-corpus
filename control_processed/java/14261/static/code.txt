public Pair<Assertion, WsFederationConfiguration> buildAndVerifyAssertion(final RequestedSecurityToken reqToken, final Collection<WsFederationConfiguration> config) {
        val securityToken = getSecurityTokenFromRequestedToken(reqToken, config);
        if (securityToken instanceof Assertion) {
            LOGGER.debug("Security token is an assertion.");
            val assertion = Assertion.class.cast(securityToken);
            LOGGER.debug("Extracted assertion successfully: [{}]", assertion);
            val cfg = config.stream()
                .filter(c -> c.getIdentityProviderIdentifier().equals(assertion.getIssuer()))
                .findFirst()
                .orElse(null);
            if (cfg == null) {
                throw new IllegalArgumentException("Could not locate wsfed configuration for security token provided. The assertion issuer "
                    + assertion.getIssuer() + " does not match any of the identity provider identifiers defined in the configuration");
            }
            return Pair.of(assertion, cfg);
        }
        throw new IllegalArgumentException("Could not extract or decrypt an assertion based on the security token provided");
    }