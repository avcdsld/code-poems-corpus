public static void terminateRpcEndpoint(RpcEndpoint rpcEndpoint, Time timeout) throws ExecutionException, InterruptedException, TimeoutException {
		rpcEndpoint.closeAsync().get(timeout.toMilliseconds(), TimeUnit.MILLISECONDS);
	}