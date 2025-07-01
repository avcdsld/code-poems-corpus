void report(Class c) {
        if (!get().contains(c)) {
            try {
                append(c.getName());
            } catch (IOException e) {
                LOGGER.log(Level.WARNING, "Failed to persist " + file, e);
            }
        }
    }