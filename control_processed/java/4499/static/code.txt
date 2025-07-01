public JaccardIndex<K, VV, EV> setGroupSize(int groupSize) {
		Preconditions.checkArgument(groupSize > 0, "Group size must be greater than zero");

		this.groupSize = groupSize;

		return this;
	}