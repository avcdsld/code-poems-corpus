@Override
	void requestSubpartition(int subpartitionIndex) throws IOException, InterruptedException {

		boolean retriggerRequest = false;

		// The lock is required to request only once in the presence of retriggered requests.
		synchronized (requestLock) {
			checkState(!isReleased, "LocalInputChannel has been released already");

			if (subpartitionView == null) {
				LOG.debug("{}: Requesting LOCAL subpartition {} of partition {}.",
					this, subpartitionIndex, partitionId);

				try {
					ResultSubpartitionView subpartitionView = partitionManager.createSubpartitionView(
						partitionId, subpartitionIndex, this);

					if (subpartitionView == null) {
						throw new IOException("Error requesting subpartition.");
					}

					// make the subpartition view visible
					this.subpartitionView = subpartitionView;

					// check if the channel was released in the meantime
					if (isReleased) {
						subpartitionView.releaseAllResources();
						this.subpartitionView = null;
					}
				} catch (PartitionNotFoundException notFound) {
					if (increaseBackoff()) {
						retriggerRequest = true;
					} else {
						throw notFound;
					}
				}
			}
		}

		// Do this outside of the lock scope as this might lead to a
		// deadlock with a concurrent release of the channel via the
		// input gate.
		if (retriggerRequest) {
			inputGate.retriggerPartitionRequest(partitionId.getPartitionId());
		}
	}