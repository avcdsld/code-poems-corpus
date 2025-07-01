def AddRunsFromDirectory(self, path, name=None):
    """Load runs from a directory; recursively walks subdirectories.

    If path doesn't exist, no-op. This ensures that it is safe to call
      `AddRunsFromDirectory` multiple times, even before the directory is made.

    Args:
      path: A string path to a directory to load runs from.
      name: Optional, specifies a name for the experiment under which the
        runs from this directory hierarchy will be imported. If omitted, the
        path will be used as the name.

    Raises:
      ValueError: If the path exists and isn't a directory.
    """
    logger.info('Starting AddRunsFromDirectory: %s (as %s)', path, name)
    for subdir in io_wrapper.GetLogdirSubdirectories(path):
      logger.info('Processing directory %s', subdir)
      if subdir not in self._run_loaders:
        logger.info('Creating DB loader for directory %s', subdir)
        names = self._get_exp_and_run_names(path, subdir, name)
        experiment_name, run_name = names
        self._run_loaders[subdir] = _RunLoader(
            subdir=subdir,
            experiment_name=experiment_name,
            run_name=run_name)
    logger.info('Done with AddRunsFromDirectory: %s', path)