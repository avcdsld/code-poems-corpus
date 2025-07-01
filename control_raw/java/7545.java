public static WatchMonitor create(Path path, int maxDepth, WatchEvent.Kind<?>... events){
		return new WatchMonitor(path, maxDepth, events);
	}