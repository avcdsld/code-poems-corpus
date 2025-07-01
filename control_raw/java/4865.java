@PublicEvolving
	public <K, S extends State, V> CompletableFuture<S> getKvState(
			final JobID jobId,
			final String queryableStateName,
			final K key,
			final TypeInformation<K> keyTypeInfo,
			final StateDescriptor<S, V> stateDescriptor) {

		return getKvState(jobId, queryableStateName, key, VoidNamespace.INSTANCE,
				keyTypeInfo, VoidNamespaceTypeInfo.INSTANCE, stateDescriptor);
	}