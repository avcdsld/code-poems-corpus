private void executeAsyncCallRunnable(Runnable runnable, String callName, boolean blocking) {
		// make sure the executor is initialized. lock against concurrent calls to this function
		synchronized (this) {
			if (executionState != ExecutionState.RUNNING) {
				return;
			}

			// get ourselves a reference on the stack that cannot be concurrently modified
			BlockingCallMonitoringThreadPool executor = this.asyncCallDispatcher;
			if (executor == null) {
				// first time use, initialize
				checkState(userCodeClassLoader != null, "userCodeClassLoader must not be null");

				// Under normal execution, we expect that one thread will suffice, this is why we
				// keep the core threads to 1. In the case of a synchronous savepoint, we will block
				// the checkpointing thread, so we need an additional thread to execute the
				// notifyCheckpointComplete() callback. Finally, we aggressively purge (potentially)
				// idle thread so that we do not risk to have many idle thread on machines with multiple
				// tasks on them. Either way, only one of them can execute at a time due to the
				// checkpoint lock.

				executor = new BlockingCallMonitoringThreadPool(
						new DispatcherThreadFactory(
							TASK_THREADS_GROUP,
							"Async calls on " + taskNameWithSubtask,
							userCodeClassLoader));
				this.asyncCallDispatcher = executor;

				// double-check for execution state, and make sure we clean up after ourselves
				// if we created the dispatcher while the task was concurrently canceled
				if (executionState != ExecutionState.RUNNING) {
					executor.shutdown();
					asyncCallDispatcher = null;
					return;
				}
			}

			LOG.debug("Invoking async call {} on task {}", callName, taskNameWithSubtask);

			try {
				executor.submit(runnable, blocking);
			}
			catch (RejectedExecutionException e) {
				// may be that we are concurrently finished or canceled.
				// if not, report that something is fishy
				if (executionState == ExecutionState.RUNNING) {
					throw new RuntimeException("Async call with a " + (blocking ? "" : "non-") + "blocking call was rejected, even though the task is running.", e);
				}
			}
		}
	}