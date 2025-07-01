public static <T> DataSet<T> sampleWithSize(
		DataSet <T> input,
		final boolean withReplacement,
		final int numSamples,
		final long seed) {

		SampleInPartition<T> sampleInPartition = new SampleInPartition<>(withReplacement, numSamples, seed);
		MapPartitionOperator mapPartitionOperator = input.mapPartition(sampleInPartition);

		// There is no previous group, so the parallelism of GroupReduceOperator is always 1.
		String callLocation = Utils.getCallLocationName();
		SampleInCoordinator<T> sampleInCoordinator = new SampleInCoordinator<>(withReplacement, numSamples, seed);
		return new GroupReduceOperator<>(mapPartitionOperator, input.getType(), sampleInCoordinator, callLocation);
	}