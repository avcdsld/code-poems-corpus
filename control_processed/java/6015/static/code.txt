public void snapshotState(StateSnapshotContext context) throws Exception {
		final KeyedStateBackend<?> keyedStateBackend = getKeyedStateBackend();
		//TODO all of this can be removed once heap-based timers are integrated with RocksDB incremental snapshots
		if (keyedStateBackend instanceof AbstractKeyedStateBackend &&
			((AbstractKeyedStateBackend<?>) keyedStateBackend).requiresLegacySynchronousTimerSnapshots()) {

			KeyedStateCheckpointOutputStream out;

			try {
				out = context.getRawKeyedOperatorStateOutput();
			} catch (Exception exception) {
				throw new Exception("Could not open raw keyed operator state stream for " +
					getOperatorName() + '.', exception);
			}

			try {
				KeyGroupsList allKeyGroups = out.getKeyGroupList();
				for (int keyGroupIdx : allKeyGroups) {
					out.startNewKeyGroup(keyGroupIdx);

					timeServiceManager.snapshotStateForKeyGroup(
						new DataOutputViewStreamWrapper(out), keyGroupIdx);
				}
			} catch (Exception exception) {
				throw new Exception("Could not write timer service of " + getOperatorName() +
					" to checkpoint state stream.", exception);
			} finally {
				try {
					out.close();
				} catch (Exception closeException) {
					LOG.warn("Could not close raw keyed operator state stream for {}. This " +
						"might have prevented deleting some state data.", getOperatorName(), closeException);
				}
			}
		}
	}