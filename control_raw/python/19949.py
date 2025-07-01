def save_bookmark(self, slot_num):
        """Save current line and position as bookmark."""
        bookmarks = CONF.get('editor', 'bookmarks')
        editorstack = self.get_current_editorstack()
        if slot_num in bookmarks:
            filename, line_num, column = bookmarks[slot_num]
            if osp.isfile(filename):
                index = editorstack.has_filename(filename)
                if index is not None:
                    block = (editorstack.tabs.widget(index).document()
                             .findBlockByNumber(line_num))
                    block.userData().bookmarks.remove((slot_num, column))
        if editorstack is not None:
            self.switch_to_plugin()
            editorstack.set_bookmark(slot_num)