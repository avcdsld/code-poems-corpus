private Path getTaskReportsFileFromId(String taskId)
  {
    return new Path(mergePaths(config.getDirectory(), taskId.replace(':', '_') + ".reports.json"));
  }