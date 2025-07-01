@Override
  public void removeProject(final Project project, final String user)
      throws ProjectManagerException {

    final long updateTime = System.currentTimeMillis();
    final String UPDATE_INACTIVE_PROJECT =
        "UPDATE projects SET active=false,modified_time=?,last_modified_by=? WHERE id=?";
    try {
      this.dbOperator.update(UPDATE_INACTIVE_PROJECT, updateTime, user, project.getId());
    } catch (final SQLException e) {
      logger.error("error remove project " + project.getName(), e);
      throw new ProjectManagerException("Error remove project " + project.getName(), e);
    }
  }