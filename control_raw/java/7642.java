public static String toJsonStr(Object obj) {
		if (null == obj) {
			return null;
		}
		if (obj instanceof String) {
			return (String) obj;
		}
		return toJsonStr(parse(obj));
	}