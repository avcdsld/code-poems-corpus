protected AuthenticationHandlerExecutionResult finalizeAuthenticationHandlerResult(final ClientCredential credentials,
                                                                                       final Principal principal,
                                                                                       final UserProfile profile,
                                                                                       final BaseClient client) {
        preFinalizeAuthenticationHandlerResult(credentials, principal, profile, client);
        return createHandlerResult(credentials, principal, new ArrayList<>(0));
    }