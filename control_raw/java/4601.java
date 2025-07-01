public static CompletableFuture<Void> nonBlockingShutdown(long timeout, TimeUnit unit, ExecutorService... executorServices) {
		return CompletableFuture.supplyAsync(
			() -> {
				gracefulShutdown(timeout, unit, executorServices);
				return null;
			});
	}