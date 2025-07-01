public Boolean pushEnabled() {
        Long value = get(SETTINGS_ENABLE_PUSH);
        if (value == null) {
            return null;
        }
        return TRUE.equals(value);
    }