public HashMap<StreamShardMetadata, SequenceNumber> snapshotState() {
		// this method assumes that the checkpoint lock is held
		assert Thread.holdsLock(checkpointLock);

		HashMap<StreamShardMetadata, SequenceNumber> stateSnapshot = new HashMap<>();
		for (KinesisStreamShardState shardWithState : subscribedShardsState) {
			stateSnapshot.put(shardWithState.getStreamShardMetadata(), shardWithState.getLastProcessedSequenceNum());
		}
		return stateSnapshot;
	}