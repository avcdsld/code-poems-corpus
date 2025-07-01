public <K> SortedGrouping<T> sortGroup(KeySelector<T, K> keySelector, Order order) {
		if (!(this.getKeys() instanceof Keys.SelectorFunctionKeys)) {
			throw new InvalidProgramException("KeySelector group-sorting keys can only be used with KeySelector grouping keys.");
		}

		TypeInformation<K> keyType = TypeExtractor.getKeySelectorTypes(keySelector, this.inputDataSet.getType());
		SortedGrouping<T> sg = new SortedGrouping<T>(this.inputDataSet, this.keys, new Keys.SelectorFunctionKeys<T, K>(keySelector, this.inputDataSet.getType(), keyType), order);
		sg.customPartitioner = getCustomPartitioner();
		return sg;
	}