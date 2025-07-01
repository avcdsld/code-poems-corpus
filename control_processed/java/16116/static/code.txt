public static synchronized void initEntityNameMap(Class<?> entityClass, Config config) {
        if (entityTableMap.get(entityClass) != null) {
            return;
        }
        //创建并缓存EntityTable
        EntityTable entityTable = resolve.resolveEntity(entityClass, config);
        entityTableMap.put(entityClass, entityTable);
    }