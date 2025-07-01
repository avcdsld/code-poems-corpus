public static int executeUpdate(PreparedStatement ps, Object... params) throws SQLException {
		StatementUtil.fillParams(ps, params);
		return ps.executeUpdate();
	}