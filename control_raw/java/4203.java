public static <T> PatternStream<T> pattern(DataStream<T> input, Pattern<T, ?> pattern) {
		return new PatternStream<>(input, pattern);
	}