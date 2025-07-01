public void setRequestWaitTime(int requestWait) {
		this.requestWait = requestWait;
		this.getConfig().setProperty(SPIDER_REQUEST_WAIT, Integer.toString(requestWait));
	}