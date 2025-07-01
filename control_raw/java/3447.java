protected void checkError() throws IOException {
		final Throwable t = cause.get();

		if (t != null) {
			if (t instanceof CancelTaskException) {
				throw (CancelTaskException) t;
			}
			if (t instanceof IOException) {
				throw (IOException) t;
			}
			else {
				throw new IOException(t);
			}
		}
	}