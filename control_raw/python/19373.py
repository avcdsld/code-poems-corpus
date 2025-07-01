def filename(self):
        """Defines the name of the configuration file to use."""
        # Needs to be done this way to be used by the project config.
        # To fix on a later PR
        self._filename = getattr(self, '_filename', None)
        self._root_path = getattr(self, '_root_path', None)

        if self._filename is None and self._root_path is None:
            return self._filename_global()
        else:
            return self._filename_projects()