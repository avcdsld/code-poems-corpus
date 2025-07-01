@Subscribe
    @SneakyThrows
    public final synchronized void renew(final ShardingRuleChangedEvent shardingRuleChangedEvent) {
        dataSource = new ShardingDataSource(dataSource.getDataSourceMap(), new OrchestrationShardingRule(shardingRuleChangedEvent.getShardingRuleConfiguration(),
                dataSource.getDataSourceMap().keySet()), dataSource.getShardingContext().getShardingProperties().getProps());
    }