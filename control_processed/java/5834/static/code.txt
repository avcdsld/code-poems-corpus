public UnionOperator<T> union(DataSet<T> other){
		return new UnionOperator<>(this, other, Utils.getCallLocationName());
	}