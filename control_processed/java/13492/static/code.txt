public static void putAvailableAuthenticationHandleNames(final RequestContext context, final Collection<String> availableHandlers) {
        context.getFlowScope().put("availableAuthenticationHandlerNames", availableHandlers);
    }