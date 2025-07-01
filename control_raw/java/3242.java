public GroupReduceOperator<T, T> first(int n) {
		if (n < 1) {
			throw new InvalidProgramException("Parameter n of first(n) must be at least 1.");
		}

		return reduceGroup(new FirstReducer<T>(n));
	}