protected CompletableFuture<?> ask(Object message, Time timeout) {
		return FutureUtils.toJava(
			Patterns.ask(rpcEndpoint, message, timeout.toMilliseconds()));
	}