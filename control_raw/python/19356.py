def path_manager_callback(self):
        """Spyder path manager"""
        from spyder.widgets.pathmanager import PathManager
        self.remove_path_from_sys_path()
        project_path = self.projects.get_pythonpath()
        dialog = PathManager(self, self.path, project_path,
                             self.not_active_path, sync=True)
        dialog.redirect_stdio.connect(self.redirect_internalshell_stdio)
        dialog.exec_()
        self.add_path_to_sys_path()
        try:
            encoding.writelines(self.path, self.SPYDER_PATH) # Saving path
            encoding.writelines(self.not_active_path,
                                self.SPYDER_NOT_ACTIVE_PATH)
        except EnvironmentError:
            pass
        self.sig_pythonpath_changed.emit()