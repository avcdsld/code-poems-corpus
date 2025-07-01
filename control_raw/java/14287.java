public long getLogoWidth() {
        try {
            val items = getLogoUrls();
            if (!items.isEmpty()) {
                return items.iterator().next().getWidth();
            }
        } catch (final Exception e) {
            LOGGER.debug(e.getMessage(), e);
        }
        return DEFAULT_IMAGE_SIZE;
    }