@SuppressWarnings("unchecked")
	@Override
	public <K, V> BroadcastState<K, V> getBroadcastState(final MapStateDescriptor<K, V> stateDescriptor) throws StateMigrationException {

		Preconditions.checkNotNull(stateDescriptor);
		String name = Preconditions.checkNotNull(stateDescriptor.getName());

		BackendWritableBroadcastState<K, V> previous =
			(BackendWritableBroadcastState<K, V>) accessedBroadcastStatesByName.get(name);

		if (previous != null) {
			checkStateNameAndMode(
					previous.getStateMetaInfo().getName(),
					name,
					previous.getStateMetaInfo().getAssignmentMode(),
					OperatorStateHandle.Mode.BROADCAST);
			return previous;
		}

		stateDescriptor.initializeSerializerUnlessSet(getExecutionConfig());
		TypeSerializer<K> broadcastStateKeySerializer = Preconditions.checkNotNull(stateDescriptor.getKeySerializer());
		TypeSerializer<V> broadcastStateValueSerializer = Preconditions.checkNotNull(stateDescriptor.getValueSerializer());

		BackendWritableBroadcastState<K, V> broadcastState =
			(BackendWritableBroadcastState<K, V>) registeredBroadcastStates.get(name);

		if (broadcastState == null) {
			broadcastState = new HeapBroadcastState<>(
					new RegisteredBroadcastStateBackendMetaInfo<>(
							name,
							OperatorStateHandle.Mode.BROADCAST,
							broadcastStateKeySerializer,
							broadcastStateValueSerializer));
			registeredBroadcastStates.put(name, broadcastState);
		} else {
			// has restored state; check compatibility of new state access

			checkStateNameAndMode(
					broadcastState.getStateMetaInfo().getName(),
					name,
					broadcastState.getStateMetaInfo().getAssignmentMode(),
					OperatorStateHandle.Mode.BROADCAST);

			RegisteredBroadcastStateBackendMetaInfo<K, V> restoredBroadcastStateMetaInfo = broadcastState.getStateMetaInfo();

			// check whether new serializers are incompatible
			TypeSerializerSchemaCompatibility<K> keyCompatibility =
				restoredBroadcastStateMetaInfo.updateKeySerializer(broadcastStateKeySerializer);
			if (keyCompatibility.isIncompatible()) {
				throw new StateMigrationException("The new key typeSerializer for broadcast state must not be incompatible.");
			}

			TypeSerializerSchemaCompatibility<V> valueCompatibility =
				restoredBroadcastStateMetaInfo.updateValueSerializer(broadcastStateValueSerializer);
			if (valueCompatibility.isIncompatible()) {
				throw new StateMigrationException("The new value typeSerializer for broadcast state must not be incompatible.");
			}

			broadcastState.setStateMetaInfo(restoredBroadcastStateMetaInfo);
		}

		accessedBroadcastStatesByName.put(name, broadcastState);
		return broadcastState;
	}