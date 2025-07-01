def build(option_hash)
      opts = option_hash.dup || {}
      @relation = @base.scoped
      opts.stringify_keys!
      opts = collapse_multiparameter_options(opts)
      assign_attributes(opts)
      self
    end