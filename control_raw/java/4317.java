private void handleCallAsync(CallAsync callAsync) {
		try {
			Object result = callAsync.getCallable().call();

			getSender().tell(new Status.Success(result), getSelf());
		} catch (Throwable e) {
			getSender().tell(new Status.Failure(e), getSelf());
		}
	}