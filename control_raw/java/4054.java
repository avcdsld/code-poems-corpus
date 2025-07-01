@Override
	public <K> AbstractKeyedStateBackend<K> createKeyedStateBackend(
		Environment env,
		JobID jobID,
		String operatorIdentifier,
		TypeSerializer<K> keySerializer,
		int numberOfKeyGroups,
		KeyGroupRange keyGroupRange,
		TaskKvStateRegistry kvStateRegistry,
		TtlTimeProvider ttlTimeProvider,
		MetricGroup metricGroup,
		@Nonnull Collection<KeyedStateHandle> stateHandles,
		CloseableRegistry cancelStreamRegistry) throws IOException {

		// first, make sure that the RocksDB JNI library is loaded
		// we do this explicitly here to have better error handling
		String tempDir = env.getTaskManagerInfo().getTmpDirectories()[0];
		ensureRocksDBIsLoaded(tempDir);

		// replace all characters that are not legal for filenames with underscore
		String fileCompatibleIdentifier = operatorIdentifier.replaceAll("[^a-zA-Z0-9\\-]", "_");

		lazyInitializeForJob(env, fileCompatibleIdentifier);

		File instanceBasePath = new File(
			getNextStoragePath(),
			"job_" + jobId + "_op_" + fileCompatibleIdentifier + "_uuid_" + UUID.randomUUID());

		LocalRecoveryConfig localRecoveryConfig =
			env.getTaskStateManager().createLocalRecoveryConfig();

		ExecutionConfig executionConfig = env.getExecutionConfig();
		StreamCompressionDecorator keyGroupCompressionDecorator = getCompressionDecorator(executionConfig);
		RocksDBKeyedStateBackendBuilder<K> builder = new RocksDBKeyedStateBackendBuilder<>(
			operatorIdentifier,
			env.getUserClassLoader(),
			instanceBasePath,
			getDbOptions(),
			stateName -> getColumnOptions(),
			kvStateRegistry,
			keySerializer,
			numberOfKeyGroups,
			keyGroupRange,
			executionConfig,
			localRecoveryConfig,
			priorityQueueStateType,
			ttlTimeProvider,
			metricGroup,
			stateHandles,
			keyGroupCompressionDecorator,
			cancelStreamRegistry
		).setEnableIncrementalCheckpointing(isIncrementalCheckpointsEnabled())
			.setEnableTtlCompactionFilter(isTtlCompactionFilterEnabled())
			.setNumberOfTransferingThreads(getNumberOfTransferingThreads())
			.setNativeMetricOptions(getMemoryWatcherOptions());
		return builder.build();
	}