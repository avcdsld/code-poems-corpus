def _set_req_to_reinstall(self, req):
        # type: (InstallRequirement) -> None
        """
        Set a requirement to be installed.
        """
        # Don't uninstall the conflict if doing a user install and the
        # conflict is not a user install.
        if not self.use_user_site or dist_in_usersite(req.satisfied_by):
            req.conflicts_with = req.satisfied_by
        req.satisfied_by = None