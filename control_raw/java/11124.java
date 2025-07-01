@Nonnull
    @SuppressFBWarnings("NP_NONNULL_RETURN_VIOLATION")
    public String getApiToken() {
        LOGGER.log(Level.FINE, "Deprecated usage of getApiToken");
        if(LOGGER.isLoggable(Level.FINER)){
            LOGGER.log(Level.FINER, "Deprecated usage of getApiToken (trace)", new Exception());
        }
        return hasPermissionToSeeToken()
                ? getApiTokenInsecure()
                : Messages.ApiTokenProperty_ChangeToken_TokenIsHidden();
    }