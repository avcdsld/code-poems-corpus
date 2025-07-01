def connect(self, **kwargs):
        """
        Connect to window and set it foreground

        Args:
            **kwargs: optional arguments

        Returns:
            None

        """
        self.app = self._app.connect(**kwargs)
        try:
            self._top_window = self.app.top_window().wrapper_object()
            self.set_foreground()
        except RuntimeError:
            self._top_window = None