public SQLRouteResult route(final String logicSQL) {
        SQLStatement sqlStatement = shardingRouter.parse(logicSQL, false);
        return masterSlaveRouter.route(shardingRouter.route(logicSQL, Collections.emptyList(), sqlStatement));
    }