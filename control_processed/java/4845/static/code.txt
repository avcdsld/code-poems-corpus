@Override
	public void grantLeadership(final UUID newLeaderSessionID) {
		final CompletableFuture<Boolean> acceptLeadershipFuture = clearStateFuture
			.thenComposeAsync((ignored) -> tryAcceptLeadership(newLeaderSessionID), getUnfencedMainThreadExecutor());

		final CompletableFuture<Void> confirmationFuture = acceptLeadershipFuture.thenAcceptAsync(
			(acceptLeadership) -> {
				if (acceptLeadership) {
					// confirming the leader session ID might be blocking,
					leaderElectionService.confirmLeaderSessionID(newLeaderSessionID);
				}