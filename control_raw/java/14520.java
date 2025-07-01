public boolean isUndefined() {
        return StringUtils.isBlank(text) || StringUtils.isBlank(from) || StringUtils.isBlank(subject);
    }