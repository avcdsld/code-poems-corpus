def _update_projects(self):
        '''Check project update'''
        now = time.time()
        if (
                not self._force_update_project
                and self._last_update_project + self.UPDATE_PROJECT_INTERVAL > now
        ):
            return
        for project in self.projectdb.check_update(self._last_update_project):
            self._update_project(project)
            logger.debug("project: %s updated.", project['name'])
        self._force_update_project = False
        self._last_update_project = now