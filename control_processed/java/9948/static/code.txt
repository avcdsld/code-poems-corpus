public static Optional<String> findTableName(final PredicateSegment predicateSegment, final SQLStatement sqlStatement, final ShardingTableMetaData shardingTableMetaData) {
        if (!(sqlStatement instanceof SelectStatement)) {
            return Optional.of(sqlStatement.getTables().getSingleTableName());
        }
        SelectStatement currentSelectStatement = (SelectStatement) sqlStatement;
        while (null != currentSelectStatement.getParentStatement()) {
            currentSelectStatement = currentSelectStatement.getParentStatement();
            Optional<String> tableName = findTableName(predicateSegment, currentSelectStatement.getTables(), shardingTableMetaData);
            if (tableName.isPresent()) {
                return tableName;
            }
        }
        return findTableName(predicateSegment, currentSelectStatement.getTables(), shardingTableMetaData);
    }