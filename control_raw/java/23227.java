public static int findAvailablePortFrom(int minPort) {
		for (int port = minPort; port < PORT_RANGE_MAX; port++) {
			if (isPortAvailable(port)) {
				return port;
			}
		}

		throw new IllegalStateException(
				String.format("Could not find an available tcp port in the range [%d, %d]", minPort, PORT_RANGE_MAX));
	}