@Nullable
	public static SSLContext createRestClientSSLContext(Configuration config) throws Exception {
		final RestSSLContextConfigMode configMode;
		if (isRestSSLAuthenticationEnabled(config)) {
			configMode = RestSSLContextConfigMode.MUTUAL;
		} else {
			configMode = RestSSLContextConfigMode.CLIENT;
		}

		return createRestSSLContext(config, configMode);
	}