def _show_details(self):
        """Show traceback on its own dialog"""
        if self.details.isVisible():
            self.details.hide()
            self.details_btn.setText(_('Show details'))
        else:
            self.resize(570, 700)
            self.details.document().setPlainText('')
            self.details.append_text_to_shell(self.error_traceback,
                                              error=True,
                                              prompt=False)
            self.details.show()
            self.details_btn.setText(_('Hide details'))