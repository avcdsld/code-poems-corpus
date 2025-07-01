public void substring(StringValue target, int start, int end) {
		target.setValue(this, start, end - start);
	}