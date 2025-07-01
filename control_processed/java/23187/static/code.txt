public static Boolean getBoolean(String propertyName, String envName, Boolean defaultValue) {
		checkEnvName(envName);
		Boolean propertyValue = BooleanUtil.toBooleanObject(System.getProperty(propertyName), null);
		if (propertyValue != null) {
			return propertyValue;
		} else {
			propertyValue = BooleanUtil.toBooleanObject(System.getenv(envName), null);
			return propertyValue != null ? propertyValue : defaultValue;
		}
	}