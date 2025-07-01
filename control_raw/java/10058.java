public Optional<ColumnDefinitionSegment> findColumnDefinition(final String columnName, final ShardingTableMetaData shardingTableMetaData) {
        Optional<ColumnDefinitionSegment> result = findColumnDefinitionFromMetaData(columnName, shardingTableMetaData);
        return result.isPresent() ? result : findColumnDefinitionFromCurrentAddClause(columnName);
    }