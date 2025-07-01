public String getString(String key, String defaultValue) {
		Object o = getRawValue(key);
		if (o == null) {
			return defaultValue;
		} else {
			return o.toString();
		}
	}