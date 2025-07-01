def signal_path(cls, project, signal):
        """Return a fully-qualified signal string."""
        return google.api_core.path_template.expand(
            "projects/{project}/signals/{signal}", project=project, signal=signal
        )