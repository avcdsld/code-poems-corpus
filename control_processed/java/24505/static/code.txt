public long getLastInsertId() throws SQLException {
    // A default connection: autocommit = true.
    long num = -1;
    try {
      num = ((Number) this.queryRunner
          .query(this.conn, "SELECT LAST_INSERT_ID();", new ScalarHandler<>(1)))
          .longValue();
    } catch (final SQLException ex) {
      logger.error("can not get last insertion ID");
      throw ex;
    }
    return num;
  }