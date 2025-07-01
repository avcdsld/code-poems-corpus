private static DirContext getDirContext() {
        Hashtable<String, String> env = new Hashtable<>();
        env.put(JAVA_NAMING_FACTORY_INITIAL, DNS_NAMING_FACTORY);
        env.put(JAVA_NAMING_PROVIDER_URL, DNS_PROVIDER_URL);

        try {
            return new InitialDirContext(env);
        } catch (Throwable e) {
            throw new RuntimeException("Cannot get dir context for some reason", e);
        }
    }