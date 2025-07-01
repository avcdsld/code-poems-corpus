@Nonnull
    public static IdStrategy idStrategy() {
        Jenkins j = Jenkins.get();
        SecurityRealm realm = j.getSecurityRealm();
        if (realm == null) {
            return IdStrategy.CASE_INSENSITIVE;
        }
        return realm.getUserIdStrategy();
    }