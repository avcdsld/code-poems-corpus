@Override
    public void registerStatsStorageListener(StatsStorageListener listener) {
        if (!this.listeners.contains(listener)) {
            this.listeners.add(listener);
        }
    }