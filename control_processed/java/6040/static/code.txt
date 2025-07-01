@Override
	public void shutdown() {
		// mark shut down and exit if it already was shut down
		if (!isShutdown.compareAndSet(false, true)) {
			return;
		}

		// Remove shutdown hook to prevent resource leaks
		ShutdownHookUtil.removeShutdownHook(shutdownHook, getClass().getSimpleName(), LOG);

		try {
			if (LOG.isDebugEnabled()) {
				LOG.debug("Shutting down I/O manager.");
			}

			// close writing and reading threads with best effort and log problems
			// first notify all to close, then wait until all are closed

			for (WriterThread wt : writers) {
				try {
					wt.shutdown();
				}
				catch (Throwable t) {
					LOG.error("Error while shutting down IO Manager writer thread.", t);
				}
			}
			for (ReaderThread rt : readers) {
				try {
					rt.shutdown();
				}
				catch (Throwable t) {
					LOG.error("Error while shutting down IO Manager reader thread.", t);
				}
			}
			try {
				for (WriterThread wt : writers) {
					wt.join();
				}
				for (ReaderThread rt : readers) {
					rt.join();
				}
			}
			catch (InterruptedException iex) {
				// ignore this on shutdown
			}
		}
		finally {
			// make sure we call the super implementation in any case and at the last point,
			// because this will clean up the I/O directories
			super.shutdown();
		}
	}