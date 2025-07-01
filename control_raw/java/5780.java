@PublicEvolving
	public DataStreamSink<T> writeAsText(String path) {
		return writeUsingOutputFormat(new TextOutputFormat<T>(new Path(path)));
	}