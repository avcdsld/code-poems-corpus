private void onDelayModify(WatchEvent<?> event, Path currentPath) {
		Path eventPath = Paths.get(currentPath.toString(), event.context().toString());
		if(eventSet.contains(eventPath)) {
			//此事件已经被触发过，后续事件忽略，等待统一处理。
			return;
		}
		
		//事件第一次触发，此时标记事件，并启动处理线程延迟处理，处理结束后会删除标记
		eventSet.add(eventPath);
		startHandleModifyThread(event, currentPath);
	}