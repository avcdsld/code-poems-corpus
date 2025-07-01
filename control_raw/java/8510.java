public void tx(VoidFunc1<Session> func) throws SQLException {
		try {
			beginTransaction();
			func.call(this);
			commit();
		} catch (Throwable e) {
			quietRollback();
			throw (e instanceof SQLException) ? (SQLException) e : new SQLException(e);
		}
	}