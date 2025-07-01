@EventListener
    public void handleRegisteredServicesLoadedEvent(final CasRegisteredServicesLoadedEvent event) {
        event.getServices()
            .stream()
            .filter(OidcRegisteredService.class::isInstance)
            .forEach(s -> {
                LOGGER.trace("Attempting to reconcile scopes and attributes for service [{}] of type [{}]",
                    s.getServiceId(), s.getClass().getSimpleName());
                this.scopeToAttributesFilter.reconcile(s);
            });
    }