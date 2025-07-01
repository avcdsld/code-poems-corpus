def clean_document(self):
        """
        Removes trailing whitespaces and ensure one single blank line at the
        end of the QTextDocument.

        FIXME: It was deprecated in pyqode, maybe It should be deleted
        """
        editor = self._editor
        value = editor.verticalScrollBar().value()
        pos = self.cursor_position()
        editor.textCursor().beginEditBlock()

        # cleanup whitespaces
        editor._cleaning = True
        eaten = 0
        removed = set()
        for line in editor._modified_lines:
            # parse line before and line after modified line (for cases where
            # key_delete or key_return has been pressed)
            for j in range(-1, 2):
                # skip current line
                if line + j != pos[0]:
                    if line + j >= 0:
                        txt = self.line_text(line + j)
                        stxt = txt.rstrip()
                        if txt != stxt:
                            self.set_line_text(line + j, stxt)
                        removed.add(line + j)
        editor._modified_lines -= removed

        # ensure there is only one blank line left at the end of the file
        i = self.line_count()
        while i:
            line = self.line_text(i - 1)
            if line.strip():
                break
            self.remove_last_line()
            i -= 1
        if self.line_text(self.line_count() - 1):
            editor.appendPlainText('')

        # restore cursor and scrollbars
        text_cursor = editor.textCursor()
        doc = editor.document()
        assert isinstance(doc, QTextDocument)
        text_cursor = self._move_cursor_to(pos[0])
        text_cursor.movePosition(text_cursor.StartOfLine,
                                 text_cursor.MoveAnchor)
        cpos = text_cursor.position()
        text_cursor.select(text_cursor.LineUnderCursor)
        if text_cursor.selectedText():
            text_cursor.setPosition(cpos)
            offset = pos[1] - eaten
            text_cursor.movePosition(text_cursor.Right, text_cursor.MoveAnchor,
                                     offset)
        else:
            text_cursor.setPosition(cpos)
        editor.setTextCursor(text_cursor)
        editor.verticalScrollBar().setValue(value)

        text_cursor.endEditBlock()
        editor._cleaning = False