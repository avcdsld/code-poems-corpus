public static TextProtocolBackendHandler newInstance(final String sql, final BackendConnection backendConnection) {
        if (sql.toUpperCase().startsWith(SCTL_SET)) {
            return new ShardingCTLSetBackendHandler(sql, backendConnection);
        }
        if (sql.toUpperCase().startsWith(SCTL_SHOW)) {
            return new ShardingCTLShowBackendHandler(sql, backendConnection);
        }
        if (sql.toUpperCase().startsWith(SCTL_EXPLAIN)) {
            return new ShardingCTLExplainBackendHandler(sql, backendConnection);
        }
        throw new IllegalArgumentException(sql);
    }