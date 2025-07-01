public static DataSource createDataSource(final byte[] yamlBytes) throws SQLException, IOException {
        YamlOrchestrationMasterSlaveRuleConfiguration config = unmarshal(yamlBytes);
        return createDataSource(config.getDataSources(), config.getMasterSlaveRule(), config.getProps(), config.getOrchestration());
    }