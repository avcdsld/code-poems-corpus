def save_initial_state(self):
        """Save initial cursors and initial active widget."""
        paths = self.paths
        self.initial_widget = self.get_widget()
        self.initial_cursors = {}

        for i, editor in enumerate(self.widgets):
            if editor is self.initial_widget:
                self.initial_path = paths[i]
            # This try is needed to make the fileswitcher work with 
            # plugins that does not have a textCursor.
            try:
                self.initial_cursors[paths[i]] = editor.textCursor()
            except AttributeError:
                pass