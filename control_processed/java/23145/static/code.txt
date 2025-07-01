public static void invokeSetter(Object obj, String propertyName, Object value) {
		Method method = getSetterMethod(obj.getClass(), propertyName, value.getClass());
		if (method == null) {
			throw new IllegalArgumentException(
					"Could not find getter method [" + propertyName + "] on target [" + obj + ']');
		}
		invokeMethod(obj, method, value);
	}