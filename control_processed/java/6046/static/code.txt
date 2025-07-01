@Override
	public Thread newThread(Runnable runnable) {
		Thread t = new Thread(group, runnable, namePrefix + threadNumber.getAndIncrement());
		t.setDaemon(true);

		t.setPriority(threadPriority);

		// optional handler for uncaught exceptions
		if (exceptionHandler != null) {
			t.setUncaughtExceptionHandler(exceptionHandler);
		}

		return t;
	}