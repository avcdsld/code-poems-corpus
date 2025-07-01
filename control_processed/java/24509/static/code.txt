public String getWorkingDirectory() {
    final String workingDir = getJobProps().getString(WORKING_DIR, this.jobPath);
    return Utils.ifNull(workingDir, "");
  }