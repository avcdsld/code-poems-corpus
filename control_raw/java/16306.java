@Override
    public long getNumberOfEvents() {
        try {
            lock.readLock().lock();
            long currentTime = System.currentTimeMillis();
            actualizeCounts(currentTime);
            return sumCounts();
        } finally {
            lock.readLock().unlock();
        }
    }