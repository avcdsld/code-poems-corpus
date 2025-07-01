protected void addAuthenticationMethodAttribute(final AuthenticationBuilder builder,
                                                    final Authentication authentication) {
        authentication.getSuccesses().values().forEach(result -> builder.addAttribute(AUTHENTICATION_METHOD_ATTRIBUTE, result.getHandlerName()));
    }