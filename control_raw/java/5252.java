public static void terminateRpcServices(
			Time timeout,
			RpcService... rpcServices) throws InterruptedException, ExecutionException, TimeoutException {
		final Collection<CompletableFuture<?>> terminationFutures = new ArrayList<>(rpcServices.length);

		for (RpcService service : rpcServices) {
			if (service != null) {
				terminationFutures.add(service.stopService());
			}
		}

		FutureUtils.waitForAll(terminationFutures).get(timeout.toMilliseconds(), TimeUnit.MILLISECONDS);
	}