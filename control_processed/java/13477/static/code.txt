public static void putAuthenticationResult(final AuthenticationResult authenticationResult, final RequestContext context) {
        context.getConversationScope().put(PARAMETER_AUTHENTICATION_RESULT, authenticationResult);
    }