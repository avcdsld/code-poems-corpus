public static FeatureCollector prototype() {
		FeatureCollector protoType = new FeatureCollector();
		protoType.setName(FeatureCollectorConstants.VERSIONONE);
		protoType.setOnline(true);
        protoType.setEnabled(true);
		protoType.setCollectorType(CollectorType.AgileTool);
		protoType.setLastExecuted(System.currentTimeMillis());

		return protoType;
	}