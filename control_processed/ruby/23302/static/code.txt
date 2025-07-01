def save_plist(filename, options = {})
      options = { :indent => DEFAULT_INDENT }.merge(options)
      Plist::Emit.save_plist(self, filename, options)
    end