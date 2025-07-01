protected void decrementLock(SessionImplementor session, Object key, Lock lock) {
        lock.unlock(region.nextTimestamp());
        region.put(session, key, lock);
    }