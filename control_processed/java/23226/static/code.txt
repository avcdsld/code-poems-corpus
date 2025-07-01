public static int findRandomAvailablePort(int minPort, int maxPort) {
		int portRange = maxPort - minPort;
		int candidatePort;
		int searchCounter = 0;

		do {
			if (++searchCounter > portRange) {
				throw new IllegalStateException(
						String.format("Could not find an available tcp port in the range [%d, %d] after %d attempts",
								minPort, maxPort, searchCounter));
			}
			candidatePort = minPort + random.nextInt(portRange + 1);
		} while (!isPortAvailable(candidatePort));

		return candidatePort;
	}