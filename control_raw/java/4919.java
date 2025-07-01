public void addBroadcastSetForApplyFunction(String name, DataSet<?> data) {
		this.bcVarsApply.add(new Tuple2<>(name, data));
	}