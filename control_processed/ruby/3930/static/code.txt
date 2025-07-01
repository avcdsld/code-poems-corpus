def add_charset
      if !body.empty?
        # Only give a warning if this isn't an attachment, has non US-ASCII and the user
        # has not specified an encoding explicitly.
        if @defaulted_charset && !body.raw_source.ascii_only? && !self.attachment?
          warning = "Non US-ASCII detected and no charset defined.\nDefaulting to UTF-8, set your own if this is incorrect.\n"
          warn(warning)
        end
        header[:content_type].parameters['charset'] = @charset
      end
    end