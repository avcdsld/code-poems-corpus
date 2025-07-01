private MapViewSerializer<T, List<Long>> getValueToOrderMapViewSerializer() {
		return new MapViewSerializer<>(
				new MapSerializer<>(
						createValueSerializer(),
						new ListSerializer<>(LongSerializer.INSTANCE)));
	}