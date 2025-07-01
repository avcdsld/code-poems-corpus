private void downloadDataForAllStateHandles(
		Map<StateHandleID, StreamStateHandle> stateHandleMap,
		Path restoreInstancePath,
		CloseableRegistry closeableRegistry) throws Exception {

		try {
			List<Runnable> runnables = createDownloadRunnables(stateHandleMap, restoreInstancePath, closeableRegistry);
			List<CompletableFuture<Void>> futures = new ArrayList<>(runnables.size());
			for (Runnable runnable : runnables) {
				futures.add(CompletableFuture.runAsync(runnable, executorService));
			}
			FutureUtils.waitForAll(futures).get();
		} catch (ExecutionException e) {
			Throwable throwable = ExceptionUtils.stripExecutionException(e);
			throwable = ExceptionUtils.stripException(throwable, RuntimeException.class);
			if (throwable instanceof IOException) {
				throw (IOException) throwable;
			} else {
				throw new FlinkRuntimeException("Failed to download data for state handles.", e);
			}
		}
	}