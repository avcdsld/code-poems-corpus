private static String getFqdnHostName(InetAddress inetAddress) {
		String fqdnHostName;
		try {
			fqdnHostName = inetAddress.getCanonicalHostName();
		} catch (Throwable t) {
			LOG.warn("Unable to determine the canonical hostname. Input split assignment (such as " +
				"for HDFS files) may be non-local when the canonical hostname is missing.");
			LOG.debug("getCanonicalHostName() Exception:", t);
			fqdnHostName = inetAddress.getHostAddress();
		}

		return fqdnHostName;
	}