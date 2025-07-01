@Nullable
	public InetSocketAddress getServerAddress() {
		synchronized (lock) {
			Preconditions.checkState(state != State.CREATED, "The RestServerEndpoint has not been started yet.");
			Channel server = this.serverChannel;

			if (server != null) {
				try {
					return ((InetSocketAddress) server.localAddress());
				} catch (Exception e) {
					log.error("Cannot access local server address", e);
				}
			}

			return null;
		}
	}