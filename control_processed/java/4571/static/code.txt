public static long calculateHeapSizeMB(long totalJavaMemorySizeMB, Configuration config) {
		Preconditions.checkArgument(totalJavaMemorySizeMB > 0);

		// subtract the Java memory used for network buffers (always off-heap)
		final long networkBufMB = NetworkEnvironmentConfiguration.calculateNetworkBufferMemory(
			totalJavaMemorySizeMB << 20, // megabytes to bytes
			config) >> 20; // bytes to megabytes
		final long remainingJavaMemorySizeMB = totalJavaMemorySizeMB - networkBufMB;

		// split the available Java memory between heap and off-heap

		final boolean useOffHeap = config.getBoolean(TaskManagerOptions.MEMORY_OFF_HEAP);

		final long heapSizeMB;
		if (useOffHeap) {

			long offHeapSize;
			String managedMemorySizeDefaultVal = TaskManagerOptions.MANAGED_MEMORY_SIZE.defaultValue();
			if (!config.getString(TaskManagerOptions.MANAGED_MEMORY_SIZE).equals(managedMemorySizeDefaultVal)) {
				try {
					offHeapSize = MemorySize.parse(config.getString(TaskManagerOptions.MANAGED_MEMORY_SIZE), MEGA_BYTES).getMebiBytes();
				} catch (IllegalArgumentException e) {
					throw new IllegalConfigurationException(
						"Could not read " + TaskManagerOptions.MANAGED_MEMORY_SIZE.key(), e);
				}
			} else {
				offHeapSize = Long.valueOf(managedMemorySizeDefaultVal);
			}

			if (offHeapSize <= 0) {
				// calculate off-heap section via fraction
				double fraction = config.getFloat(TaskManagerOptions.MANAGED_MEMORY_FRACTION);
				offHeapSize = (long) (fraction * remainingJavaMemorySizeMB);
			}

			ConfigurationParserUtils.checkConfigParameter(offHeapSize < remainingJavaMemorySizeMB, offHeapSize,
				TaskManagerOptions.MANAGED_MEMORY_SIZE.key(),
					"Managed memory size too large for " + networkBufMB +
						" MB network buffer memory and a total of " + totalJavaMemorySizeMB +
						" MB JVM memory");

			heapSizeMB = remainingJavaMemorySizeMB - offHeapSize;
		} else {
			heapSizeMB = remainingJavaMemorySizeMB;
		}

		return heapSizeMB;
	}