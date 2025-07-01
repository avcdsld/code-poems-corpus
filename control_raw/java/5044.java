public <X> DataSource<X> fromCollection(Collection<X> data) {
		if (data == null) {
			throw new IllegalArgumentException("The data must not be null.");
		}
		if (data.size() == 0) {
			throw new IllegalArgumentException("The size of the collection must not be empty.");
		}

		X firstValue = data.iterator().next();

		TypeInformation<X> type = TypeExtractor.getForObject(firstValue);
		CollectionInputFormat.checkCollection(data, type.getTypeClass());
		return new DataSource<>(this, new CollectionInputFormat<>(data, type.createSerializer(config)), type, Utils.getCallLocationName());
	}