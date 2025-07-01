@Override
	public void start(LeaderRetrievalListener listener) {
		checkNotNull(listener, "Listener must not be null.");

		synchronized (startStopLock) {
			checkState(!started, "StandaloneLeaderRetrievalService can only be started once.");
			started = true;

			// directly notify the listener, because we already know the leading JobManager's address
			listener.notifyLeaderAddress(leaderAddress, leaderId);
		}
	}