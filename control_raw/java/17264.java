public boolean getBoolean(String name, boolean defaultValue) {
        String valueString = get(name);
        return "true".equals(valueString) || !"false".equals(valueString) && defaultValue;
    }