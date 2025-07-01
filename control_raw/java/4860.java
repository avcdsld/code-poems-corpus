public static List<List<OperatorStateHandle>> applyRepartitioner(
		OperatorStateRepartitioner opStateRepartitioner,
		List<List<OperatorStateHandle>> chainOpParallelStates,
		int oldParallelism,
		int newParallelism) {

		if (chainOpParallelStates == null) {
			return Collections.emptyList();
		}

		return opStateRepartitioner.repartitionState(
			chainOpParallelStates,
			oldParallelism,
			newParallelism);
		}