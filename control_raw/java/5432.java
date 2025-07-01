private <T> void addEntry(StreamElementQueueEntry<T> streamElementQueueEntry) {
		assert(lock.isHeldByCurrentThread());

		if (streamElementQueueEntry.isWatermark()) {
			lastSet = new HashSet<>(capacity);

			if (firstSet.isEmpty()) {
				firstSet.add(streamElementQueueEntry);
			} else {
				Set<StreamElementQueueEntry<?>> watermarkSet = new HashSet<>(1);
				watermarkSet.add(streamElementQueueEntry);
				uncompletedQueue.offer(watermarkSet);
			}
			uncompletedQueue.offer(lastSet);
		} else {
			lastSet.add(streamElementQueueEntry);
		}

		streamElementQueueEntry.onComplete(
			(StreamElementQueueEntry<T> value) -> {
				try {
					onCompleteHandler(value);
				} catch (InterruptedException e) {
					// The accept executor thread got interrupted. This is probably cause by
					// the shutdown of the executor.
					LOG.debug("AsyncBufferEntry could not be properly completed because the " +
						"executor thread has been interrupted.", e);
				} catch (Throwable t) {
					operatorActions.failOperator(new Exception("Could not complete the " +
						"stream element queue entry: " + value + '.', t));
				}
			},
			executor);

		numberEntries++;
	}