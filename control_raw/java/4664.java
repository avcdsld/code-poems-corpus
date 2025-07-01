public <V, A extends Serializable> void addAccumulator(String name, Accumulator<V, A> accumulator) {
		getRuntimeContext().addAccumulator(id + SEPARATOR + name, accumulator);
	}