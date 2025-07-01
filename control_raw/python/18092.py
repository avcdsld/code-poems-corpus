def atomic_download(handle,
                    download_fn,
                    module_dir,
                    lock_file_timeout_sec=10 * 60):
  """Returns the path to a Module directory for a given TF-Hub Module handle.

  Args:
    handle: (string) Location of a TF-Hub Module.
    download_fn: Callback function that actually performs download. The callback
                 receives two arguments, handle and the location of a temporary
                 directory to download the content into.
    module_dir: Directory where to download the module files to.
    lock_file_timeout_sec: The amount of time we give the current holder of
                           the lock to make progress in downloading a module.
                           If no progress is made, the lock is revoked.

  Returns:
    A string containing the path to a TF-Hub Module directory.

  Raises:
    ValueError: if the Module is not found.
  """
  lock_file = _lock_filename(module_dir)
  task_uid = uuid.uuid4().hex
  lock_contents = _lock_file_contents(task_uid)
  tmp_dir = _temp_download_dir(module_dir, task_uid)

  # Attempt to protect against cases of processes being cancelled with
  # KeyboardInterrupt by using a try/finally clause to remove the lock
  # and tmp_dir.
  try:
    while True:
      try:
        tf_utils.atomic_write_string_to_file(lock_file, lock_contents,
                                             overwrite=False)
        # Must test condition again, since another process could have created
        # the module and deleted the old lock file since last test.
        if tf_v1.gfile.Exists(module_dir):
          # Lock file will be deleted in the finally-clause.
          return module_dir
        break  # Proceed to downloading the module.
      except tf.errors.OpError:
        pass

      # Wait for lock file to disappear.
      _wait_for_lock_to_disappear(handle, lock_file, lock_file_timeout_sec)
      # At this point we either deleted a lock or a lock got removed by the
      # owner or another process. Perform one more iteration of the while-loop,
      # we would either terminate due tf_v1.gfile.Exists(module_dir) or because
      # we would obtain a lock ourselves, or wait again for the lock to
      # disappear.

    # Lock file acquired.
    logging.info("Downloading TF-Hub Module '%s'.", handle)
    tf_v1.gfile.MakeDirs(tmp_dir)
    download_fn(handle, tmp_dir)
    # Write module descriptor to capture information about which module was
    # downloaded by whom and when. The file stored at the same level as a
    # directory in order to keep the content of the 'model_dir' exactly as it
    # was define by the module publisher.
    #
    # Note: The descriptor is written purely to help the end-user to identify
    # which directory belongs to which module. The descriptor is not part of the
    # module caching protocol and no code in the TF-Hub library reads its
    # content.
    _write_module_descriptor_file(handle, module_dir)
    try:
      tf_v1.gfile.Rename(tmp_dir, module_dir)
      logging.info("Downloaded TF-Hub Module '%s'.", handle)
    except tf.errors.AlreadyExistsError:
      logging.warning("Module already exists in %s", module_dir)

  finally:
    try:
      # Temp directory is owned by the current process, remove it.
      tf_v1.gfile.DeleteRecursively(tmp_dir)
    except tf.errors.NotFoundError:
      pass
    try:
      contents = tf_utils.read_file_to_string(lock_file)
    except tf.errors.NotFoundError:
      contents = ""
    if contents == lock_contents:
      # Lock file exists and is owned by this process.
      try:
        tf_v1.gfile.Remove(lock_file)
      except tf.errors.NotFoundError:
        pass

  return module_dir