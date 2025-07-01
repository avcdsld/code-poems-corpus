public static <T> DataSet<LongValue> count(DataSet<T> input) {
		return input
			.map(new MapTo<>(new LongValue(1)))
				.returns(LONG_VALUE_TYPE_INFO)
				.name("Emit 1")
			.reduce(new AddLongValue())
				.name("Sum");
	}