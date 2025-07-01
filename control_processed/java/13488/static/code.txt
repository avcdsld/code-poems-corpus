public static Authentication getInProgressAuthentication() {
        val context = RequestContextHolder.getRequestContext();
        val authentication = context != null ? WebUtils.getAuthentication(context) : null;
        if (authentication == null) {
            return AuthenticationCredentialsThreadLocalBinder.getInProgressAuthentication();
        }
        return authentication;
    }