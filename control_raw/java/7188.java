public List<Entity> findAll(String tableName) throws SQLException {
		return findAll(Entity.create(tableName));
	}