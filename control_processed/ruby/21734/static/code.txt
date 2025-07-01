def apply(target, options = {})
      Interception.new(
        self,
        target,
        self.class.storage.default_options.merge(options)
      ).apply
    end