public CompletableFuture<Void> scheduleAll(
			SlotProvider slotProvider,
			boolean queued,
			LocationPreferenceConstraint locationPreferenceConstraint,
			@Nonnull Set<AllocationID> allPreviousExecutionGraphAllocationIds) {

		final ExecutionVertex[] vertices = this.taskVertices;

		final ArrayList<CompletableFuture<Void>> scheduleFutures = new ArrayList<>(vertices.length);

		// kick off the tasks
		for (ExecutionVertex ev : vertices) {
			scheduleFutures.add(ev.scheduleForExecution(
				slotProvider,
				queued,
				locationPreferenceConstraint,
				allPreviousExecutionGraphAllocationIds));
		}

		return FutureUtils.waitForAll(scheduleFutures);
	}