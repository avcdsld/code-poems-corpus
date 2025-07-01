public static StringifiedAccumulatorResult[] stringifyAccumulatorResults(Map<String, OptionalFailure<Accumulator<?, ?>>> accs) {
		if (accs == null || accs.isEmpty()) {
			return new StringifiedAccumulatorResult[0];
		}
		else {
			StringifiedAccumulatorResult[] results = new StringifiedAccumulatorResult[accs.size()];

			int i = 0;
			for (Map.Entry<String, OptionalFailure<Accumulator<?, ?>>> entry : accs.entrySet()) {
				results[i++] = stringifyAccumulatorResult(entry.getKey(), entry.getValue());
			}
			return results;
		}
	}