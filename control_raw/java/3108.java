protected <V> CompletableFuture<V> callAsync(Callable<V> callable, Time timeout) {
		return rpcServer.callAsync(callable, timeout);
	}