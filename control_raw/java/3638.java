public <OUT> DataStreamSource<OUT> fromCollection(Iterator<OUT> data, TypeInformation<OUT> typeInfo) {
		Preconditions.checkNotNull(data, "The iterator must not be null");

		SourceFunction<OUT> function = new FromIteratorFunction<>(data);
		return addSource(function, "Collection Source", typeInfo);
	}