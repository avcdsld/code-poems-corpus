public static ParameterizedType toParameterizedType(Type type) {
		if (type instanceof ParameterizedType) {
			return (ParameterizedType) type;
		} else if (type instanceof Class) {
			return toParameterizedType(((Class<?>) type).getGenericSuperclass());
		}
		return null;
	}