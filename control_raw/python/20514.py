def _execute(self, operation):  # type: (Operation) -> None
        """
        Execute a given operation.
        """
        method = operation.job_type

        getattr(self, "_execute_{}".format(method))(operation)