private void completePendingCheckpoint(PendingCheckpoint pendingCheckpoint) throws CheckpointException {
		final long checkpointId = pendingCheckpoint.getCheckpointId();
		final CompletedCheckpoint completedCheckpoint;

		// As a first step to complete the checkpoint, we register its state with the registry
		Map<OperatorID, OperatorState> operatorStates = pendingCheckpoint.getOperatorStates();
		sharedStateRegistry.registerAll(operatorStates.values());

		try {
			try {
				completedCheckpoint = pendingCheckpoint.finalizeCheckpoint();
			}
			catch (Exception e1) {
				// abort the current pending checkpoint if we fails to finalize the pending checkpoint.
				if (!pendingCheckpoint.isDiscarded()) {
					pendingCheckpoint.abort(CheckpointFailureReason.FINALIZE_CHECKPOINT_FAILURE, e1);
				}

				throw new CheckpointException("Could not finalize the pending checkpoint " + checkpointId + '.',
					CheckpointFailureReason.FINALIZE_CHECKPOINT_FAILURE, e1);
			}

			// the pending checkpoint must be discarded after the finalization
			Preconditions.checkState(pendingCheckpoint.isDiscarded() && completedCheckpoint != null);

			try {
				completedCheckpointStore.addCheckpoint(completedCheckpoint);
			} catch (Exception exception) {
				// we failed to store the completed checkpoint. Let's clean up
				executor.execute(new Runnable() {
					@Override
					public void run() {
						try {
							completedCheckpoint.discardOnFailedStoring();
						} catch (Throwable t) {
							LOG.warn("Could not properly discard completed checkpoint {}.", completedCheckpoint.getCheckpointID(), t);
						}
					}
				});

				throw new CheckpointException("Could not complete the pending checkpoint " + checkpointId + '.',
					CheckpointFailureReason.FINALIZE_CHECKPOINT_FAILURE, exception);
			}
		} finally {
			pendingCheckpoints.remove(checkpointId);

			triggerQueuedRequests();
		}

		rememberRecentCheckpointId(checkpointId);

		// drop those pending checkpoints that are at prior to the completed one
		dropSubsumedCheckpoints(checkpointId);

		// record the time when this was completed, to calculate
		// the 'min delay between checkpoints'
		lastCheckpointCompletionNanos = System.nanoTime();

		LOG.info("Completed checkpoint {} for job {} ({} bytes in {} ms).", checkpointId, job,
			completedCheckpoint.getStateSize(), completedCheckpoint.getDuration());

		if (LOG.isDebugEnabled()) {
			StringBuilder builder = new StringBuilder();
			builder.append("Checkpoint state: ");
			for (OperatorState state : completedCheckpoint.getOperatorStates().values()) {
				builder.append(state);
				builder.append(", ");
			}
			// Remove last two chars ", "
			builder.setLength(builder.length() - 2);

			LOG.debug(builder.toString());
		}

		// send the "notify complete" call to all vertices
		final long timestamp = completedCheckpoint.getTimestamp();

		for (ExecutionVertex ev : tasksToCommitTo) {
			Execution ee = ev.getCurrentExecutionAttempt();
			if (ee != null) {
				ee.notifyCheckpointComplete(checkpointId, timestamp);
			}
		}
	}