TaskDeploymentDescriptor createDeploymentDescriptor(
			ExecutionAttemptID executionId,
			LogicalSlot targetSlot,
			@Nullable JobManagerTaskRestore taskRestore,
			int attemptNumber) throws ExecutionGraphException {

		// Produced intermediate results
		List<ResultPartitionDeploymentDescriptor> producedPartitions = new ArrayList<>(resultPartitions.size());

		// Consumed intermediate results
		List<InputGateDeploymentDescriptor> consumedPartitions = new ArrayList<>(inputEdges.length);

		boolean lazyScheduling = getExecutionGraph().getScheduleMode().allowLazyDeployment();

		for (IntermediateResultPartition partition : resultPartitions.values()) {

			List<List<ExecutionEdge>> consumers = partition.getConsumers();

			if (consumers.isEmpty()) {
				//TODO this case only exists for test, currently there has to be exactly one consumer in real jobs!
				producedPartitions.add(ResultPartitionDeploymentDescriptor.from(
						partition,
						KeyGroupRangeAssignment.UPPER_BOUND_MAX_PARALLELISM,
						lazyScheduling));
			} else {
				Preconditions.checkState(1 == consumers.size(),
						"Only one consumer supported in the current implementation! Found: " + consumers.size());

				List<ExecutionEdge> consumer = consumers.get(0);
				ExecutionJobVertex vertex = consumer.get(0).getTarget().getJobVertex();
				int maxParallelism = vertex.getMaxParallelism();
				producedPartitions.add(ResultPartitionDeploymentDescriptor.from(partition, maxParallelism, lazyScheduling));
			}
		}

		final InputChannelDeploymentDescriptor[] icddArray = new InputChannelDeploymentDescriptor[0];

		for (ExecutionEdge[] edges : inputEdges) {
			List<InputChannelDeploymentDescriptor> partitions = InputChannelDeploymentDescriptor.fromEdges(
				Arrays.asList(edges),
				lazyScheduling);

			// If the produced partition has multiple consumers registered, we
			// need to request the one matching our sub task index.
			// TODO Refactor after removing the consumers from the intermediate result partitions
			int numConsumerEdges = edges[0].getSource().getConsumers().get(0).size();

			int queueToRequest = subTaskIndex % numConsumerEdges;

			IntermediateResult consumedIntermediateResult = edges[0].getSource().getIntermediateResult();
			final IntermediateDataSetID resultId = consumedIntermediateResult.getId();
			final ResultPartitionType partitionType = consumedIntermediateResult.getResultType();

			consumedPartitions.add(new InputGateDeploymentDescriptor(resultId, partitionType, queueToRequest, partitions.toArray(icddArray)));
		}

		final Either<SerializedValue<JobInformation>, PermanentBlobKey> jobInformationOrBlobKey = getExecutionGraph().getJobInformationOrBlobKey();

		final TaskDeploymentDescriptor.MaybeOffloaded<JobInformation> serializedJobInformation;

		if (jobInformationOrBlobKey.isLeft()) {
			serializedJobInformation = new TaskDeploymentDescriptor.NonOffloaded<>(jobInformationOrBlobKey.left());
		} else {
			serializedJobInformation = new TaskDeploymentDescriptor.Offloaded<>(jobInformationOrBlobKey.right());
		}

		final Either<SerializedValue<TaskInformation>, PermanentBlobKey> taskInformationOrBlobKey;

		try {
			taskInformationOrBlobKey = jobVertex.getTaskInformationOrBlobKey();
		} catch (IOException e) {
			throw new ExecutionGraphException(
				"Could not create a serialized JobVertexInformation for " +
					jobVertex.getJobVertexId(), e);
		}

		final TaskDeploymentDescriptor.MaybeOffloaded<TaskInformation> serializedTaskInformation;

		if (taskInformationOrBlobKey.isLeft()) {
			serializedTaskInformation = new TaskDeploymentDescriptor.NonOffloaded<>(taskInformationOrBlobKey.left());
		} else {
			serializedTaskInformation = new TaskDeploymentDescriptor.Offloaded<>(taskInformationOrBlobKey.right());
		}

		return new TaskDeploymentDescriptor(
			getJobId(),
			serializedJobInformation,
			serializedTaskInformation,
			executionId,
			targetSlot.getAllocationId(),
			subTaskIndex,
			attemptNumber,
			targetSlot.getPhysicalSlotNumber(),
			taskRestore,
			producedPartitions,
			consumedPartitions);
	}