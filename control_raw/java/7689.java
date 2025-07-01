public WeightRandom<T> add(T obj, double weight) {
		return add(new WeightObj<T>(obj, weight));
	}