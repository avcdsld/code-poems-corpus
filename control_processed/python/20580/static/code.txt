def remove(self, path, recursive=True):
        """
        Remove file or directory at location ``path``.

        :param path: a path within the FileSystem to remove.
        :type path: str
        :param recursive: if the path is a directory, recursively remove the directory and
                          all of its descendants. Defaults to ``True``.
        :type recursive: bool
        """
        self._connect()

        if self.sftp:
            self._sftp_remove(path, recursive)
        else:
            self._ftp_remove(path, recursive)

        self._close()