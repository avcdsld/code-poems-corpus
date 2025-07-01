def do_autosave(self):
        """Instruct current editorstack to autosave files where necessary."""
        logger.debug('Autosave triggered')
        stack = self.editor.get_current_editorstack()
        stack.autosave.autosave_all()
        self.start_autosave_timer()