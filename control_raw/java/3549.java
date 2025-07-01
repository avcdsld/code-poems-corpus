private void removeContender(EmbeddedLeaderElectionService service) {
		synchronized (lock) {
			// if the service was not even started, simply do nothing
			if (!service.running || shutdown) {
				return;
			}

			try {
				if (!allLeaderContenders.remove(service)) {
					throw new IllegalStateException("leader election service does not belong to this service");
				}

				// stop the service
				service.contender = null;
				service.running = false;
				service.isLeader = false;

				// if that was the current leader, unset its status
				if (currentLeaderConfirmed == service) {
					currentLeaderConfirmed = null;
					currentLeaderSessionId = null;
					currentLeaderAddress = null;
				}
				if (currentLeaderProposed == service) {
					currentLeaderProposed = null;
					currentLeaderSessionId = null;
				}

				updateLeader().whenComplete((aVoid, throwable) -> {
					if (throwable != null) {
						fatalError(throwable);
					}
				});
			}
			catch (Throwable t) {
				fatalError(t);
			}
		}
	}