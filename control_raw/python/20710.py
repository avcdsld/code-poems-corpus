def get_target(cls, scheme, path, fragment, username,
                   password, hostname, port, query, **kwargs):
        """Override this method to use values from the parsed uri to initialize
        the expected target.

        """
        raise NotImplementedError("get_target must be overridden")