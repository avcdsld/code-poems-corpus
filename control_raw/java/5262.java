@Deprecated
	public void addFirstInput(Operator<IN1>... input) {
		this.input1 = Operator.createUnionCascade(this.input1, input);
	}