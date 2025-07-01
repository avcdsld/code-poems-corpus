public final boolean unregisterCloseable(C closeable) {

		if (null == closeable) {
			return false;
		}

		synchronized (getSynchronizationLock()) {
			return doUnRegister(closeable, closeableToRef);
		}
	}