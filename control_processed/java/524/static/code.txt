public MongoClient createMongoClient(MongoClientOptions options) {
		Integer embeddedPort = getEmbeddedPort();
		if (embeddedPort != null) {
			return createEmbeddedMongoClient(options, embeddedPort);
		}
		return createNetworkMongoClient(options);
	}