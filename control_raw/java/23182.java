public static Double getDouble(String propertyName, Double defaultValue) {
		Double propertyValue = NumberUtil.toDoubleObject(System.getProperty(propertyName), null);
		return propertyValue != null ? propertyValue : defaultValue;
	}