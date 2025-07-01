public OperatorSubtaskState putSubtaskStateByOperatorID(
		@Nonnull OperatorID operatorID,
		@Nonnull OperatorSubtaskState state) {

		return subtaskStatesByOperatorID.put(operatorID, Preconditions.checkNotNull(state));
	}