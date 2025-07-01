public void addTableShardingValue(final String logicTable, final Comparable<?> value) {
        tableShardingValues.put(logicTable, value);
        databaseShardingOnly = false;
    }