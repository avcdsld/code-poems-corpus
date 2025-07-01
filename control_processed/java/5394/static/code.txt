@Deprecated
	public <R> SingleOutputStreamOperator<R> apply(R initialValue, FoldFunction<T, R> foldFunction, WindowFunction<R, R, K, W> function) {

		TypeInformation<R> resultType = TypeExtractor.getFoldReturnTypes(foldFunction, input.getType(),
			Utils.getCallLocationName(), true);

		return apply(initialValue, foldFunction, function, resultType);
	}