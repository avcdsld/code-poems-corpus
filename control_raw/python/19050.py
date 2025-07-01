def move_editorstack_data(self, start, end):
        """Reorder editorstack.data so it is synchronized with the tab bar when
        tabs are moved."""
        if start < 0 or end < 0:
            return
        else:
            steps = abs(end - start)
            direction = (end-start) // steps  # +1 for right, -1 for left

        data = self.data
        self.blockSignals(True)

        for i in range(start, end, direction):
            data[i], data[i+direction] = data[i+direction], data[i]

        self.blockSignals(False)
        self.refresh()