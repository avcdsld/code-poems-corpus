public static ContaineredTaskManagerParameters create(
			Configuration config,
			long containerMemoryMB,
			int numSlots) {
		// (1) try to compute how much memory used by container
		final long cutoffMB = calculateCutoffMB(config, containerMemoryMB);

		// (2) split the remaining Java memory between heap and off-heap
		final long heapSizeMB = TaskManagerServices.calculateHeapSizeMB(containerMemoryMB - cutoffMB, config);
		// use the cut-off memory for off-heap (that was its intention)
		final long offHeapSizeMB = containerMemoryMB - heapSizeMB;

		// (3) obtain the additional environment variables from the configuration
		final HashMap<String, String> envVars = new HashMap<>();
		final String prefix = ResourceManagerOptions.CONTAINERIZED_TASK_MANAGER_ENV_PREFIX;

		for (String key : config.keySet()) {
			if (key.startsWith(prefix) && key.length() > prefix.length()) {
				// remove prefix
				String envVarKey = key.substring(prefix.length());
				envVars.put(envVarKey, config.getString(key, null));
			}
		}

		// done
		return new ContaineredTaskManagerParameters(
			containerMemoryMB, heapSizeMB, offHeapSizeMB, numSlots, envVars);
	}