@Deprecated
	public static <T> Utils.ChecksumHashCode checksumHashCode(DataSet<T> input) throws Exception {
		final String id = new AbstractID().toString();

		input.output(new Utils.ChecksumHashCodeHelper<T>(id)).name("ChecksumHashCode");

		JobExecutionResult res = input.getExecutionEnvironment().execute();
		return res.<Utils.ChecksumHashCode> getAccumulatorResult(id);
	}