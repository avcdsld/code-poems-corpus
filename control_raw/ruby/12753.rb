def extends(file, options = {}, &block)
        return unless resolve_condition(options)

        options = @options.slice(:child_root).merge!(:object => @_object).merge!(options)
        engines << partial_as_engine(file, options, &block)
      end