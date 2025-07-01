@EventListener
    public void logAuthenticationPrincipalResolvedEvent(final CasAuthenticationPrincipalResolvedEvent e) {
        LOGGER.debug(PRINCIPAL_RESOLVED_MSG, e.getPrincipal().getId(), e.getPrincipal().getAttributes());
    }