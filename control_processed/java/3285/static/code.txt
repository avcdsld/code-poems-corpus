@Override
	public void onTaskFailure(Execution taskExecution, Throwable cause) {

		executionGraph.getJobMasterMainThreadExecutor().assertRunningInMainThread();

		// to better handle the lack of resources (potentially by a scale-in), we
		// make failures due to missing resources global failures 
		if (cause instanceof NoResourceAvailableException) {
			LOG.info("Not enough resources to schedule {} - triggering full recovery.", taskExecution);
			executionGraph.failGlobal(cause);
			return;
		}

		LOG.info("Recovering task failure for {} (#{}) via individual restart.", 
				taskExecution.getVertex().getTaskNameWithSubtaskIndex(), taskExecution.getAttemptNumber());

		numTaskFailures.inc();

		// trigger the restart once the task has reached its terminal state
		// Note: currently all tasks passed here are already in their terminal state,
		//       so we could actually avoid the future. We use it anyways because it is cheap and
		//       it helps to support better testing
		final CompletableFuture<ExecutionState> terminationFuture = taskExecution.getTerminalStateFuture();
		terminationFuture.thenRun(
			() -> performExecutionVertexRestart(taskExecution.getVertex(), taskExecution.getGlobalModVersion()));
	}