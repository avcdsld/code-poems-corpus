public boolean toBoolean(String name, boolean defaultValue) {
        String property = getProperties().getProperty(name);
        return property != null ? Boolean.parseBoolean(property) : defaultValue;
    }