public AggregateOperator<T> aggregate(Aggregations agg, int field) {
		return new AggregateOperator<>(this, agg, field, Utils.getCallLocationName());
	}