public static <T, U extends T> CompletableFuture<T> toJava(Future<U> scalaFuture) {
		final CompletableFuture<T> result = new CompletableFuture<>();

		scalaFuture.onComplete(new OnComplete<U>() {
			@Override
			public void onComplete(Throwable failure, U success) {
				if (failure != null) {
					result.completeExceptionally(failure);
				} else {
					result.complete(success);
				}
			}
		}, Executors.directExecutionContext());

		return result;
	}