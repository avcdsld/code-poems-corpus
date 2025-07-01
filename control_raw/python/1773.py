def open(self, mode='a', **kwargs):
        """
        Open the file in the specified mode

        Parameters
        ----------
        mode : {'a', 'w', 'r', 'r+'}, default 'a'
            See HDFStore docstring or tables.open_file for info about modes
        """
        tables = _tables()

        if self._mode != mode:

            # if we are changing a write mode to read, ok
            if self._mode in ['a', 'w'] and mode in ['r', 'r+']:
                pass
            elif mode in ['w']:

                # this would truncate, raise here
                if self.is_open:
                    raise PossibleDataLossError(
                        "Re-opening the file [{0}] with mode [{1}] "
                        "will delete the current file!"
                        .format(self._path, self._mode)
                    )

            self._mode = mode

        # close and reopen the handle
        if self.is_open:
            self.close()

        if self._complevel and self._complevel > 0:
            self._filters = _tables().Filters(self._complevel, self._complib,
                                              fletcher32=self._fletcher32)

        try:
            self._handle = tables.open_file(self._path, self._mode, **kwargs)
        except (IOError) as e:  # pragma: no cover
            if 'can not be written' in str(e):
                print(
                    'Opening {path} in read-only mode'.format(path=self._path))
                self._handle = tables.open_file(self._path, 'r', **kwargs)
            else:
                raise

        except (ValueError) as e:

            # trap PyTables >= 3.1 FILE_OPEN_POLICY exception
            # to provide an updated message
            if 'FILE_OPEN_POLICY' in str(e):
                e = ValueError(
                    "PyTables [{version}] no longer supports opening multiple "
                    "files\n"
                    "even in read-only mode on this HDF5 version "
                    "[{hdf_version}]. You can accept this\n"
                    "and not open the same file multiple times at once,\n"
                    "upgrade the HDF5 version, or downgrade to PyTables 3.0.0 "
                    "which allows\n"
                    "files to be opened multiple times at once\n"
                    .format(version=tables.__version__,
                            hdf_version=tables.get_hdf5_version()))

            raise e

        except (Exception) as e:

            # trying to read from a non-existent file causes an error which
            # is not part of IOError, make it one
            if self._mode == 'r' and 'Unable to open/create file' in str(e):
                raise IOError(str(e))
            raise