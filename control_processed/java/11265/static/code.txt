@CheckForNull
    public static Boolean optBoolean(String name) {
        String v = getString(name);
        return v == null ? null : Boolean.parseBoolean(v);
    }