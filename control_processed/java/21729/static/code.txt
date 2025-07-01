@Write
    public String[] refresh(@Nullable Boolean force) {

        if (force != null && force) {
            eventPublisher.publishEvent(new RefreshEvent());
            return new String[0];
        } else {
            Map<String, Object> changes = environment.refreshAndDiff();
            if (!changes.isEmpty()) {
                eventPublisher.publishEvent(new RefreshEvent(changes));
            }
            Set<String> keys = changes.keySet();
            return keys.toArray(new String[0]);
        }
    }