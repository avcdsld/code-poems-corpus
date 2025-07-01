public long getLong(String name, long defaultValue) {
        String valueString = get(name);
        if (valueString == null)
            return defaultValue;
        try {
            String hexString = getHexDigits(valueString);
            if (hexString != null) {
                return Long.parseLong(hexString, 16);
            }
            return Long.parseLong(valueString);
        } catch (NumberFormatException e) {
            return defaultValue;
        }
    }