private boolean shouldRoll(BucketState<T> bucketState, long currentProcessingTime) throws IOException {
		boolean shouldRoll = false;
		int subtaskIndex = getRuntimeContext().getIndexOfThisSubtask();
		if (!bucketState.isWriterOpen) {
			shouldRoll = true;
			LOG.debug("BucketingSink {} starting new bucket.", subtaskIndex);
		} else {
			long writePosition = bucketState.writer.getPos();
			if (writePosition > batchSize) {
				shouldRoll = true;
				LOG.debug(
					"BucketingSink {} starting new bucket because file position {} is above batch size {}.",
					subtaskIndex,
					writePosition,
					batchSize);
			} else {
				if (currentProcessingTime - bucketState.creationTime > batchRolloverInterval) {
					shouldRoll = true;
					LOG.debug(
						"BucketingSink {} starting new bucket because file is older than roll over interval {}.",
						subtaskIndex,
						batchRolloverInterval);
				}
			}
		}
		return shouldRoll;
	}