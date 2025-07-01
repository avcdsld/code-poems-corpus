public int insert(Entity record) throws SQLException {
		Connection conn = null;
		try {
			conn = this.getConnection();
			return runner.insert(conn, record);
		} catch (SQLException e) {
			throw e;
		} finally {
			this.closeConnection(conn);
		}
	}