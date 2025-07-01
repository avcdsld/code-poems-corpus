public static <T> DataSet<Tuple2<Integer, Long>> countElementsPerPartition(DataSet<T> input) {
		return input.mapPartition(new RichMapPartitionFunction<T, Tuple2<Integer, Long>>() {
			@Override
			public void mapPartition(Iterable<T> values, Collector<Tuple2<Integer, Long>> out) throws Exception {
				long counter = 0;
				for (T value : values) {
					counter++;
				}
				out.collect(new Tuple2<>(getRuntimeContext().getIndexOfThisSubtask(), counter));
			}
		});
	}