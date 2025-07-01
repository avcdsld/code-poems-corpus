private boolean shouldRoll() throws IOException {
		boolean shouldRoll = false;
		int subtaskIndex = getRuntimeContext().getIndexOfThisSubtask();
		if (!isWriterOpen) {
			shouldRoll = true;
			LOG.debug("RollingSink {} starting new initial bucket. ", subtaskIndex);
		}
		if (bucketer.shouldStartNewBucket(new Path(basePath), currentBucketDirectory)) {
			shouldRoll = true;
			LOG.debug("RollingSink {} starting new bucket because {} said we should. ", subtaskIndex, bucketer);
			// we will retrieve a new bucket base path in openNewPartFile so reset the part counter
			partCounter = 0;
		}
		if (isWriterOpen) {
			long writePosition = writer.getPos();
			if (isWriterOpen && writePosition > batchSize) {
				shouldRoll = true;
				LOG.debug(
						"RollingSink {} starting new bucket because file position {} is above batch size {}.",
						subtaskIndex,
						writePosition,
						batchSize);
			}
		}
		return shouldRoll;
	}