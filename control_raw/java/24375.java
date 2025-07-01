public int update(final String updateClause, final Object... params) throws SQLException {
    try {
      return this.queryRunner.update(updateClause, params);
    } catch (final SQLException ex) {
      // todo kunkun-tang: Retry logics should be implemented here.
      logger.error("update failed", ex);
      if (this.dbMetrics != null) {
        this.dbMetrics.markDBFailUpdate();
      }
      throw ex;
    }
  }