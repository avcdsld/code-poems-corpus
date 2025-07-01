protected void executeWithTransaction(String query, ExecuteFunction function) {
        withTransaction(tx -> execute(tx, query, function));
    }