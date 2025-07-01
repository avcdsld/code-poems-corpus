public AuthenticationBuilder setCredentials(final @NonNull List<CredentialMetaData> credentials) {
        this.credentials.clear();
        this.credentials.addAll(credentials);
        return this;
    }