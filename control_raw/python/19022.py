def remove(self, tab_index):
        """Remove the widget at the corresponding tab_index."""
        _id = id(self.editor.tabs.widget(tab_index))
        if _id in self.history:
            self.history.remove(_id)