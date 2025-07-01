private boolean locationAwareLog(int level_int, Throwable t, String msgTemplate, Object[] arguments) {
		return locationAwareLog(FQCN, level_int, t, msgTemplate, arguments);
	}