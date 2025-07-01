public static <K, V> Map<K, V> notEmpty(Map<K, V> map, String errorMsgTemplate, Object... params) throws IllegalArgumentException {
		if (CollectionUtil.isEmpty(map)) {
			throw new IllegalArgumentException(StrUtil.format(errorMsgTemplate, params));
		}
		return map;
	}