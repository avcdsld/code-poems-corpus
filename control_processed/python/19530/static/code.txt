def is_empty(self):
        """Return whether the block of user data is empty."""
        return (not self.breakpoint and not self.code_analysis
                and not self.todo and not self.bookmarks)