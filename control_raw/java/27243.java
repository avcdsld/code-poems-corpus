public Principal authenticate(List<String> authHeader) throws AuthException {
        if (isAuthEnabled()) {
            String credentials = parseCredentials(authHeader);
            return pravegaAuthManager.authenticate(credentials);
        }
        return null;
    }