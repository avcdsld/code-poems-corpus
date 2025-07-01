def symlink(self, source, dest):
        """
        Create a symbolic link to the ``source`` path at ``destination``.

        :param str source: path of the original file
        :param str dest: path of the newly created symlink
        """
        dest = self._adjust_cwd(dest)
        self._log(DEBUG, "symlink({!r}, {!r})".format(source, dest))
        source = b(source)
        self._request(CMD_SYMLINK, source, dest)