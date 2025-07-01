public static SingleInputGate create(
		String owningTaskName,
		JobID jobId,
		InputGateDeploymentDescriptor igdd,
		NetworkEnvironment networkEnvironment,
		TaskEventPublisher taskEventPublisher,
		TaskActions taskActions,
		InputChannelMetrics metrics,
		Counter numBytesInCounter) {

		final IntermediateDataSetID consumedResultId = checkNotNull(igdd.getConsumedResultId());
		final ResultPartitionType consumedPartitionType = checkNotNull(igdd.getConsumedPartitionType());

		final int consumedSubpartitionIndex = igdd.getConsumedSubpartitionIndex();
		checkArgument(consumedSubpartitionIndex >= 0);

		final InputChannelDeploymentDescriptor[] icdd = checkNotNull(igdd.getInputChannelDeploymentDescriptors());

		final NetworkEnvironmentConfiguration networkConfig = networkEnvironment.getConfiguration();

		final SingleInputGate inputGate = new SingleInputGate(
			owningTaskName, jobId, consumedResultId, consumedPartitionType, consumedSubpartitionIndex,
			icdd.length, taskActions, numBytesInCounter, networkConfig.isCreditBased());

		// Create the input channels. There is one input channel for each consumed partition.
		final InputChannel[] inputChannels = new InputChannel[icdd.length];

		int numLocalChannels = 0;
		int numRemoteChannels = 0;
		int numUnknownChannels = 0;

		for (int i = 0; i < inputChannels.length; i++) {
			final ResultPartitionID partitionId = icdd[i].getConsumedPartitionId();
			final ResultPartitionLocation partitionLocation = icdd[i].getConsumedPartitionLocation();

			if (partitionLocation.isLocal()) {
				inputChannels[i] = new LocalInputChannel(inputGate, i, partitionId,
					networkEnvironment.getResultPartitionManager(),
					taskEventPublisher,
					networkConfig.partitionRequestInitialBackoff(),
					networkConfig.partitionRequestMaxBackoff(),
					metrics
				);

				numLocalChannels++;
			}
			else if (partitionLocation.isRemote()) {
				inputChannels[i] = new RemoteInputChannel(inputGate, i, partitionId,
					partitionLocation.getConnectionId(),
					networkEnvironment.getConnectionManager(),
					networkConfig.partitionRequestInitialBackoff(),
					networkConfig.partitionRequestMaxBackoff(),
					metrics
				);

				numRemoteChannels++;
			}
			else if (partitionLocation.isUnknown()) {
				inputChannels[i] = new UnknownInputChannel(inputGate, i, partitionId,
					networkEnvironment.getResultPartitionManager(),
					taskEventPublisher,
					networkEnvironment.getConnectionManager(),
					networkConfig.partitionRequestInitialBackoff(),
					networkConfig.partitionRequestMaxBackoff(),
					metrics
				);

				numUnknownChannels++;
			}
			else {
				throw new IllegalStateException("Unexpected partition location.");
			}

			inputGate.setInputChannel(partitionId.getPartitionId(), inputChannels[i]);
		}

		LOG.debug("{}: Created {} input channels (local: {}, remote: {}, unknown: {}).",
			owningTaskName,
			inputChannels.length,
			numLocalChannels,
			numRemoteChannels,
			numUnknownChannels);

		return inputGate;
	}