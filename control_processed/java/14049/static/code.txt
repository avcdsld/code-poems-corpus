public List<CouchDbGoogleAuthenticatorAccount> findByUsername(final String username) {
        try {
            return queryView("by_username", username);
        } catch (final DocumentNotFoundException ignored) {
            return null;
        }
    }