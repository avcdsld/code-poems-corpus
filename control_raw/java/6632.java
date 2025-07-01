public static Method[] getMethods(Class<?> clazz, Filter<Method> filter) throws SecurityException {
		if (null == clazz) {
			return null;
		}
		return ArrayUtil.filter(getMethods(clazz), filter);
	}