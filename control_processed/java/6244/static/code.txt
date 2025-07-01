private void enqueueAvailableReader(final NetworkSequenceViewReader reader) throws Exception {
		if (reader.isRegisteredAsAvailable() || !reader.isAvailable()) {
			return;
		}
		// Queue an available reader for consumption. If the queue is empty,
		// we try trigger the actual write. Otherwise this will be handled by
		// the writeAndFlushNextMessageIfPossible calls.
		boolean triggerWrite = availableReaders.isEmpty();
		registerAvailableReader(reader);

		if (triggerWrite) {
			writeAndFlushNextMessageIfPossible(ctx.channel());
		}
	}