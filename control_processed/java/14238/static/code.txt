private static boolean doesNameMatchPattern(final Principal principal, final Pattern pattern) {
        if (pattern != null) {
            val name = principal.getName();
            val result = pattern.matcher(name).matches();
            LOGGER.debug("[{}] matches [{}] == [{}]", pattern.pattern(), name, result);
            return result;
        }
        return true;
    }