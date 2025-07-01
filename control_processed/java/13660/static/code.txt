private Optional<RegisteredService> getRegisteredServiceFromRequest(final HttpServletRequest request) {
        val service = this.argumentExtractor.extractService(request);
        if (service != null) {
            val resolved = authenticationRequestServiceSelectionStrategies.resolveService(service);
            return Optional.ofNullable(this.servicesManager.findServiceBy(resolved));
        }
        return Optional.empty();
    }