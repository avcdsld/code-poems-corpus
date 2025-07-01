public void start() {
		lock.lock();
		try {
			if (State.NOT_STARTED.equals(state)) {
				spiderThread.addSpiderListener(this);
				spiderThread.start();
				state = State.RUNNING;
				SpiderEventPublisher.publishScanEvent(
						ScanEventPublisher.SCAN_STARTED_EVENT, this.scanId, this.target, user);
			}
		} finally {
			lock.unlock();
		}
	}