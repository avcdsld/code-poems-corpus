private boolean transitionState(ExecutionState currentState, ExecutionState newState, Throwable cause) {
		if (STATE_UPDATER.compareAndSet(this, currentState, newState)) {
			if (cause == null) {
				LOG.info("{} ({}) switched from {} to {}.", taskNameWithSubtask, executionId, currentState, newState);
			} else {
				LOG.info("{} ({}) switched from {} to {}.", taskNameWithSubtask, executionId, currentState, newState, cause);
			}

			return true;
		} else {
			return false;
		}
	}