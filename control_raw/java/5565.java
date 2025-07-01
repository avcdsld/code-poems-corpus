public static StateBackend loadStateBackendFromConfig(
			Configuration config,
			ClassLoader classLoader,
			@Nullable Logger logger) throws IllegalConfigurationException, DynamicCodeLoadingException, IOException {

		checkNotNull(config, "config");
		checkNotNull(classLoader, "classLoader");

		final String backendName = config.getString(CheckpointingOptions.STATE_BACKEND);
		if (backendName == null) {
			return null;
		}

		// by default the factory class is the backend name 
		String factoryClassName = backendName;

		switch (backendName.toLowerCase()) {
			case MEMORY_STATE_BACKEND_NAME:
				MemoryStateBackend memBackend = new MemoryStateBackendFactory().createFromConfig(config, classLoader);

				if (logger != null) {
					Path memExternalized = memBackend.getCheckpointPath();
					String extern = memExternalized == null ? "" :
							" (externalized to " + memExternalized + ')';
					logger.info("State backend is set to heap memory (checkpoint to JobManager) {}", extern);
				}
				return memBackend;

			case FS_STATE_BACKEND_NAME:
				FsStateBackend fsBackend = new FsStateBackendFactory().createFromConfig(config, classLoader);
				if (logger != null) {
					logger.info("State backend is set to heap memory (checkpoints to filesystem \"{}\")",
							fsBackend.getCheckpointPath());
				}
				return fsBackend;

			case ROCKSDB_STATE_BACKEND_NAME:
				factoryClassName = "org.apache.flink.contrib.streaming.state.RocksDBStateBackendFactory";
				// fall through to the 'default' case that uses reflection to load the backend
				// that way we can keep RocksDB in a separate module

			default:
				if (logger != null) {
					logger.info("Loading state backend via factory {}", factoryClassName);
				}

				StateBackendFactory<?> factory;
				try {
					@SuppressWarnings("rawtypes")
					Class<? extends StateBackendFactory> clazz =
							Class.forName(factoryClassName, false, classLoader)
									.asSubclass(StateBackendFactory.class);

					factory = clazz.newInstance();
				}
				catch (ClassNotFoundException e) {
					throw new DynamicCodeLoadingException(
							"Cannot find configured state backend factory class: " + backendName, e);
				}
				catch (ClassCastException | InstantiationException | IllegalAccessException e) {
					throw new DynamicCodeLoadingException("The class configured under '" +
							CheckpointingOptions.STATE_BACKEND.key() + "' is not a valid state backend factory (" +
							backendName + ')', e);
				}

				return factory.createFromConfig(config, classLoader);
		}
	}