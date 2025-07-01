public void triggerReload() {
		synchronized (this.monitor) {
			synchronized (this.connections) {
				for (Connection connection : this.connections) {
					try {
						connection.triggerReload();
					}
					catch (Exception ex) {
						logger.debug("Unable to send reload message", ex);
					}
				}
			}
		}
	}