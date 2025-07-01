def download_and_uncompress(self, fileobj, dst_path):
    """Streams the content for the 'fileobj' and stores the result in dst_path.

    Args:
      fileobj: File handle pointing to .tar/.tar.gz content.
      dst_path: Absolute path where to store uncompressed data from 'fileobj'.

    Raises:
      ValueError: Unknown object encountered inside the TAR file.
    """
    try:
      with tarfile.open(mode="r|*", fileobj=fileobj) as tgz:
        for tarinfo in tgz:
          abs_target_path = _merge_relative_path(dst_path, tarinfo.name)

          if tarinfo.isfile():
            self._extract_file(tgz, tarinfo, abs_target_path)
          elif tarinfo.isdir():
            tf_v1.gfile.MakeDirs(abs_target_path)
          else:
            # We do not support symlinks and other uncommon objects.
            raise ValueError(
                "Unexpected object type in tar archive: %s" % tarinfo.type)

        total_size_str = tf_utils.bytes_to_readable_str(
            self._total_bytes_downloaded, True)
        self._print_download_progress_msg(
            "Downloaded %s, Total size: %s" % (self._url, total_size_str),
            flush=True)
    except tarfile.ReadError:
      raise IOError("%s does not appear to be a valid module." % self._url)