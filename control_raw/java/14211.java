@DeleteOperation
    public boolean revokeConsents(@Selector final String principal, @Selector final long decisionId) {
        LOGGER.debug("Deleting consent decisions for principal [{}].", principal);
        return this.consentRepository.deleteConsentDecision(decisionId, principal);
    }