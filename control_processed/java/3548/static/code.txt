private void addContender(EmbeddedLeaderElectionService service, LeaderContender contender) {
		synchronized (lock) {
			checkState(!shutdown, "leader election service is shut down");
			checkState(!service.running, "leader election service is already started");

			try {
				if (!allLeaderContenders.add(service)) {
					throw new IllegalStateException("leader election service was added to this service multiple times");
				}

				service.contender = contender;
				service.running = true;

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