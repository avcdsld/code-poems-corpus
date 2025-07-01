@SuppressWarnings("unchecked")
	public SingleOutputStreamOperator<T> reduce(ReduceFunction<T> function) {
		if (function instanceof RichFunction) {
			throw new UnsupportedOperationException("ReduceFunction of reduce can not be a RichFunction. " +
					"Please use reduce(ReduceFunction, WindowFunction) instead.");
		}

		//clean the closure
		function = input.getExecutionEnvironment().clean(function);

		String callLocation = Utils.getCallLocationName();
		String udfName = "AllWindowedStream." + callLocation;

		return reduce(function, new PassThroughAllWindowFunction<W, T>());
	}