@Override
	public RocksDBRestoreResult restore() throws Exception {

		if (restoreStateHandles == null || restoreStateHandles.isEmpty()) {
			return null;
		}

		final KeyedStateHandle theFirstStateHandle = restoreStateHandles.iterator().next();

		boolean isRescaling = (restoreStateHandles.size() > 1 ||
			!Objects.equals(theFirstStateHandle.getKeyGroupRange(), keyGroupRange));

		if (isRescaling) {
			restoreWithRescaling(restoreStateHandles);
		} else {
			restoreWithoutRescaling(theFirstStateHandle);
		}
		return new RocksDBRestoreResult(this.db, defaultColumnFamilyHandle,
			nativeMetricMonitor, lastCompletedCheckpointId, backendUID, restoredSstFiles);
	}