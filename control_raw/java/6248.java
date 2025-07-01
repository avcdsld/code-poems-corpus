@Override
	public void setInputType(TypeInformation<?> type, ExecutionConfig executionConfig) {
		if (!type.isTupleType()) {
			throw new InvalidProgramException("The " + ScalaCsvOutputFormat.class.getSimpleName() +
				" can only be used to write tuple data sets.");
		}
	}