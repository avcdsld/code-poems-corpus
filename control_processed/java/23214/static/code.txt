public static Boolean toBooleanObject(String str, Boolean defaultValue) {
		return str != null ? Boolean.valueOf(str) : defaultValue;
	}