def remove_temporary_source(self):
        # type: () -> None
        """Remove the source files from this requirement, if they are marked
        for deletion"""
        if self.source_dir and os.path.exists(
                os.path.join(self.source_dir, PIP_DELETE_MARKER_FILENAME)):
            logger.debug('Removing source in %s', self.source_dir)
            rmtree(self.source_dir)
        self.source_dir = None
        self._temp_build_dir.cleanup()
        self.build_env.cleanup()