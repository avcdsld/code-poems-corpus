@Override
	public long getEstimatedOutputSize() {
		long estimate = this.source.template.getEstimatedOutputSize();
		return estimate < 0 ? estimate : estimate * this.replicationFactor;
	}