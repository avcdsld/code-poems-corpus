public static Log replay(Log source, Class<?> destination) {
		return replay(source, LogFactory.getLog(destination));
	}