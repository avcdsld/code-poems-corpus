public WindowedStream<T, KEY, GlobalWindow> countWindow(long size) {
		return window(GlobalWindows.create()).trigger(PurgingTrigger.of(CountTrigger.of(size)));
	}