private static <IN, K> org.apache.flink.api.common.operators.SingleInputOperator<?, IN, ?> translateSelectorFunctionDistinct(
			SelectorFunctionKeys<IN, ?> rawKeys,
			ReduceFunction<IN> function,
			TypeInformation<IN> outputType,
			String name,
			Operator<IN> input,
			int parallelism,
			CombineHint hint) {
		@SuppressWarnings("unchecked")
		final SelectorFunctionKeys<IN, K> keys = (SelectorFunctionKeys<IN, K>) rawKeys;

		TypeInformation<Tuple2<K, IN>> typeInfoWithKey = KeyFunctions.createTypeWithKey(keys);
		Operator<Tuple2<K, IN>> keyedInput = KeyFunctions.appendKeyExtractor(input, keys);

		PlanUnwrappingReduceOperator<IN, K> reducer =
				new PlanUnwrappingReduceOperator<>(function, keys, name, outputType, typeInfoWithKey);
		reducer.setInput(keyedInput);
		reducer.setCombineHint(hint);
		reducer.setParallelism(parallelism);

		return KeyFunctions.appendKeyRemover(reducer, keys);
	}