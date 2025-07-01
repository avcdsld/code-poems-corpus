def schedule(self, callback, *args, **kwargs):
        """Schedule the callback to be called asynchronously in a thread pool.

        Args:
            callback (Callable): The function to call.
            args: Positional arguments passed to the function.
            kwargs: Key-word arguments passed to the function.

        Returns:
            None
        """
        self._executor.submit(callback, *args, **kwargs)