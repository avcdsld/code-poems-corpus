@Deprecated
	public DataStreamSource<String> socketTextStream(String hostname, int port, char delimiter, long maxRetry) {
		return socketTextStream(hostname, port, String.valueOf(delimiter), maxRetry);
	}