public static OAuthRegisteredService getRegisteredOAuthServiceByRedirectUri(final ServicesManager servicesManager, final String redirectUri) {
        return getRegisteredOAuthServiceByPredicate(servicesManager, s -> s.matches(redirectUri));
    }