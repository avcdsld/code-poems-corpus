def cut
      str = selection_text
      unless str.empty?
        Clipboard.copy str
        self.selection_text = '' if editable?
      end
    end