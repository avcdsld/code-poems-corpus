public int start() throws IOException {
		synchronized (this.monitor) {
			Assert.state(!isStarted(), "Server already started");
			logger.debug("Starting live reload server on port " + this.port);
			this.serverSocket = new ServerSocket(this.port);
			int localPort = this.serverSocket.getLocalPort();
			this.listenThread = this.threadFactory.newThread(this::acceptConnections);
			this.listenThread.setDaemon(true);
			this.listenThread.setName("Live Reload Server");
			this.listenThread.start();
			return localPort;
		}
	}