public SplitDataProperties<T> splitsGroupedBy(String groupFields) {

		if (groupFields == null) {
			throw new InvalidProgramException("GroupFields may not be null.");
		}

		String[] groupKeysA = groupFields.split(";");
		if (groupKeysA.length == 0) {
			throw new InvalidProgramException("GroupFields may not be empty.");
		}

		if (this.splitOrdering != null) {
			throw new InvalidProgramException("DataSource may either be grouped or sorted.");
		}

		this.splitGroupKeys = getAllFlatKeys(groupKeysA);

		return this;
	}