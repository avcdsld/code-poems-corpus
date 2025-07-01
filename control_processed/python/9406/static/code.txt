def is_file(self):
        """
        Whether this path is a regular file (also True for symlinks pointing
        to regular files).
        """
        try:
            return S_ISREG(self.stat().st_mode)
        except OSError as e:
            if e.errno not in (ENOENT, ENOTDIR):
                raise
            # Path doesn't exist or is a broken symlink
            # (see https://bitbucket.org/pitrou/pathlib/issue/12/)
            return False