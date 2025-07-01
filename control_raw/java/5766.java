@PublicEvolving
	public <R extends Tuple> SingleOutputStreamOperator<R> project(int... fieldIndexes) {
		return new StreamProjection<>(this, fieldIndexes).projectTupleX();
	}