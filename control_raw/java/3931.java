protected boolean registerAllRequestsProcessedListener(NotificationListener listener) throws IOException {
		checkNotNull(listener);

		synchronized (listenerLock) {
			if (allRequestsProcessedListener == null) {
				// There was a race with the processing of the last outstanding request
				if (requestsNotReturned.get() == 0) {
					return false;
				}

				allRequestsProcessedListener = listener;

				return true;
			}
		}

		throw new IllegalStateException("Already subscribed.");
	}