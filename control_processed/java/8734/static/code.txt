public static String getMessage(Throwable e) {
		if (null == e) {
			return NULL;
		}
		return StrUtil.format("{}: {}", e.getClass().getSimpleName(), e.getMessage());
	}