public CompletableFuture<AccessExecutionGraph> getExecutionGraph(JobID jobId, RestfulGateway restfulGateway) {
		return getExecutionGraphInternal(jobId, restfulGateway).thenApply(Function.identity());
	}