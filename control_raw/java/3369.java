public static void main(String[] args) {
		try {
			// startup checks and logging
			EnvironmentInformation.logEnvironmentInfo(LOG, "ZooKeeper Quorum Peer", args);
			
			final ParameterTool params = ParameterTool.fromArgs(args);
			final String zkConfigFile = params.getRequired("zkConfigFile");
			final int peerId = params.getInt("peerId");

			// Run quorum peer
			runFlinkZkQuorumPeer(zkConfigFile, peerId);
		}
		catch (Throwable t) {
			LOG.error("Error running ZooKeeper quorum peer: " + t.getMessage(), t);
			System.exit(-1);
		}
	}