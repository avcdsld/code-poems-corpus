@Deprecated
	@SuppressWarnings("deprecation")
	@PublicEvolving
	public StreamExecutionEnvironment enableCheckpointing(long interval, CheckpointingMode mode, boolean force) {
		checkpointCfg.setCheckpointingMode(mode);
		checkpointCfg.setCheckpointInterval(interval);
		checkpointCfg.setForceCheckpointing(force);
		return this;
	}