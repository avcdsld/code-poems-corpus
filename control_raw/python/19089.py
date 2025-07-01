def advance_cell(self, reverse=False):
        """Advance to the next cell.

        reverse = True --> go to previous cell.
        """
        if not reverse:
            move_func = self.get_current_editor().go_to_next_cell
        else:
            move_func = self.get_current_editor().go_to_previous_cell

        if self.focus_to_editor:
            move_func()
        else:
            term = QApplication.focusWidget()
            move_func()
            term.setFocus()
            term = QApplication.focusWidget()
            move_func()
            term.setFocus()