public static <T, F> FieldAugment<T, F> circularSafeAugment(Class<T> type, Class<? super F> fieldType, String name) {
		checkNotNull(type, "type");
		checkNotNull(fieldType, "fieldType");
		checkNotNull(name, "name");
		
		@SuppressWarnings("unchecked")
		F defaultValue = (F) getDefaultValue(fieldType);
		FieldAugment<T, F> ret = tryCreateReflectionAugment(type, fieldType, name, defaultValue);
		return ret != null ? ret : new MapWeakFieldAugment<T, F>(defaultValue);
	}