public void addMasterState(MasterState state) {
		checkNotNull(state);

		synchronized (lock) {
			if (!discarded) {
				masterState.add(state);
			}
		}
	}