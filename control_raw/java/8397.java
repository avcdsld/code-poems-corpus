public <T> List<T> toList(Class<T> elementType) {
		return JSONConverter.toList(this, elementType);
	}