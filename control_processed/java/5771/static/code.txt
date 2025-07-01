public AllWindowedStream<T, GlobalWindow> countWindowAll(long size) {
		return windowAll(GlobalWindows.create()).trigger(PurgingTrigger.of(CountTrigger.of(size)));
	}