private static InjectionPattern getInjectionPattern(String contents) {
        if (contents == null || contents.trim().equals("")) {
            return null;
        }
        InjectionPattern injectionPattern = new InjectionPattern();
        contents = contents.trim();
        // Retrieve key, default value and error text
        String[] array = contents.split(":", 2);
        array[0] = array[0].trim();
        if ("".equals(array[0])) {
            return null;
        }
        // Set key of the injectionPattern
        injectionPattern.setKey(array[0]);
        if (array.length == 2) {
            // Adding space after colon is enabled, so trim is needed
            array[1] = array[1].trim();
            // Set error text
            if (array[1].startsWith("?")) {
                injectionPattern.setErrorText(array[1].substring(1));
            } else if (array[1].startsWith("$")) {
                // Skip this injection when "$" is only character found after the ":"
                if (array[1].length() == 1) {
                    injectionPattern.setDefaultValue("\\$\\{" + array[0] + "\\}");
                    // Otherwise, treat as a default value
                    // Add "\\" since $ is a special character
                } else {
                    injectionPattern.setDefaultValue("\\" + array[1]);
                }
                // Set default value
            } else {
                injectionPattern.setDefaultValue(array[1]);
            }
        }
        return injectionPattern;
    }