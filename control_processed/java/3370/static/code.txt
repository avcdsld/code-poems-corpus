public static void runFlinkZkQuorumPeer(String zkConfigFile, int peerId) throws Exception {

		Properties zkProps = new Properties();

		try (InputStream inStream = new FileInputStream(new File(zkConfigFile))) {
			zkProps.load(inStream);
		}

		LOG.info("Configuration: " + zkProps);

		// Set defaults for required properties
		setRequiredProperties(zkProps);

		// Write peer id to myid file
		writeMyIdToDataDir(zkProps, peerId);

		// The myid file needs to be written before creating the instance. Otherwise, this
		// will fail.
		QuorumPeerConfig conf = new QuorumPeerConfig();
		conf.parseProperties(zkProps);

		if (conf.isDistributed()) {
			// Run quorum peer
			LOG.info("Running distributed ZooKeeper quorum peer (total peers: {}).",
					conf.getServers().size());

			QuorumPeerMain qp = new QuorumPeerMain();
			qp.runFromConfig(conf);
		}
		else {
			// Run standalone
			LOG.info("Running standalone ZooKeeper quorum peer.");

			ZooKeeperServerMain zk = new ZooKeeperServerMain();
			ServerConfig sc = new ServerConfig();
			sc.readFrom(conf);
			zk.runFromConfig(sc);
		}
	}