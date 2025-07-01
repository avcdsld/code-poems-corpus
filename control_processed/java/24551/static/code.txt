void deleteProjectDirsIfNecessary(final long newProjectSizeInBytes) {
    final long projectCacheMaxSizeInByte =
        (long) (this.projectCacheDir.getTotalSpace() * this.percentageOfDisk);

    final long start = System.currentTimeMillis();
    final List<ProjectDirectoryMetadata> allProjects = loadAllProjects();
    log.info("Loading {} project dirs metadata completed in {} sec(s)",
        allProjects.size(), (System.currentTimeMillis() - start) / 1000);

    final long currentSpaceInBytes = getProjectDirsTotalSizeInBytes(allProjects);
    if (currentSpaceInBytes + newProjectSizeInBytes >= projectCacheMaxSizeInByte) {
      log.info(
          "Project cache usage[{} MB] >= cache limit[{} MB], start cleaning up project dirs",
          (currentSpaceInBytes + newProjectSizeInBytes) / (1024 * 1024),
          projectCacheMaxSizeInByte / (1024 * 1024));

      final long freeCacheSpaceInBytes = projectCacheMaxSizeInByte - currentSpaceInBytes;

      deleteLeastRecentlyUsedProjects(newProjectSizeInBytes - freeCacheSpaceInBytes, allProjects);
    }
  }