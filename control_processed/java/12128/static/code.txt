void setTemporaryOfflineCause(OfflineCause cause) {
        try {
            if (temporaryOfflineCause != cause) {
                temporaryOfflineCause = cause;
                save();
            }
        } catch (java.io.IOException e) {
            LOGGER.warning("Unable to complete save, temporary offline status will not be persisted: " + e.getMessage());
        }
    }