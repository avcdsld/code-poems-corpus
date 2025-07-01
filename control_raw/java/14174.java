public static boolean doesResourceExist(final String location) {
        try {
            return getResourceFrom(location) != null;
        } catch (final Exception e) {
            LOGGER.trace(e.getMessage(), e);
        }
        return false;
    }