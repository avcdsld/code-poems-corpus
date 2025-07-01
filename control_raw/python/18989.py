def show_plain_text(self, text):
        """Show text in plain mode"""
        self.switch_to_plugin()
        self.switch_to_plain_text()
        self.set_plain_text(text, is_code=False)