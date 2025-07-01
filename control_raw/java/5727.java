@Override
	protected org.apache.flink.api.common.operators.SingleInputOperator<T, T, ?> translateToDataFlow(Operator<T> input) {
		// All the translation magic happens when the iteration end is encountered.
		throw new InvalidProgramException("A data set that is part of an iteration was used as a sink or action."
				+ " Did you forget to close the iteration?");
	}