def browse_history(self, backward):
        """Browse history"""
        if self.is_cursor_before('eol') and self.hist_wholeline:
            self.hist_wholeline = False
        tocursor = self.get_current_line_to_cursor()
        text, self.histidx = self.find_in_history(tocursor, self.histidx,
                                                  backward)
        if text is not None:
            if self.hist_wholeline:
                self.clear_line()
                self.insert_text(text)
            else:
                cursor_position = self.get_position('cursor')
                # Removing text from cursor to the end of the line
                self.remove_text('cursor', 'eol')
                # Inserting history text
                self.insert_text(text)
                self.set_cursor_position(cursor_position)