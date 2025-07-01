protected static boolean locateMatchingAttributeBasedOnAuthenticationAttributes(
        final MultifactorAuthenticationProviderBypassProperties bypass, final Authentication authn) {
        return locateMatchingAttributeValue(bypass.getAuthenticationAttributeName(),
            bypass.getAuthenticationAttributeValue(), authn.getAttributes(), false);
    }