def remove_local_zip(self):
        """
        Remove our local zip file.
        """

        if self.stage_config.get('delete_local_zip', True):
            try:
                if os.path.isfile(self.zip_path):
                    os.remove(self.zip_path)
                if self.handler_path and os.path.isfile(self.handler_path):
                    os.remove(self.handler_path)
            except Exception as e: # pragma: no cover
                sys.exit(-1)