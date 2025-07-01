public StringifiedAccumulatorResult[] getAggregatedUserAccumulatorsStringified() {
		Map<String, OptionalFailure<Accumulator<?, ?>>> userAccumulators = new HashMap<>();

		for (ExecutionVertex vertex : taskVertices) {
			Map<String, Accumulator<?, ?>> next = vertex.getCurrentExecutionAttempt().getUserAccumulators();
			if (next != null) {
				AccumulatorHelper.mergeInto(userAccumulators, next);
			}
		}

		return StringifiedAccumulatorResult.stringifyAccumulatorResults(userAccumulators);
	}