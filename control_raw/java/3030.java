public static QueryableStateConfiguration fromConfiguration(Configuration config) {
		if (!config.getBoolean(QueryableStateOptions.ENABLE_QUERYABLE_STATE_PROXY_SERVER)) {
			return null;
		}

		final Iterator<Integer> proxyPorts = NetUtils.getPortRangeFromString(
			config.getString(QueryableStateOptions.PROXY_PORT_RANGE));
		final Iterator<Integer> serverPorts = NetUtils.getPortRangeFromString(
			config.getString(QueryableStateOptions.SERVER_PORT_RANGE));

		final int numProxyServerNetworkThreads = config.getInteger(QueryableStateOptions.PROXY_NETWORK_THREADS);
		final int numProxyServerQueryThreads = config.getInteger(QueryableStateOptions.PROXY_ASYNC_QUERY_THREADS);

		final int numStateServerNetworkThreads = config.getInteger(QueryableStateOptions.SERVER_NETWORK_THREADS);
		final int numStateServerQueryThreads = config.getInteger(QueryableStateOptions.SERVER_ASYNC_QUERY_THREADS);

		return new QueryableStateConfiguration(
			proxyPorts,
			serverPorts,
			numProxyServerNetworkThreads,
			numProxyServerQueryThreads,
			numStateServerNetworkThreads,
			numStateServerQueryThreads);
	}