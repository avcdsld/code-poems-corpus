static void adjustAutoCommitConfig(Properties properties, OffsetCommitMode offsetCommitMode) {
		if (offsetCommitMode == OffsetCommitMode.ON_CHECKPOINTS || offsetCommitMode == OffsetCommitMode.DISABLED) {
			properties.setProperty(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, "false");
		}
	}