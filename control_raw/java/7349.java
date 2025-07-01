public CronPattern getPattern(int index) {
		final Lock readLock = lock.readLock();
		try {
			readLock.lock();
			return patterns.get(index);
		} finally {
			readLock.unlock();
		}
	}