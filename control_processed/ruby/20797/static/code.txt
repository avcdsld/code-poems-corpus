def def_set(*method_names)
      method_names.each do |method_name|
        define_singleton_method method_name do |arg = Undefined, &block|
          if arg.equal?(Undefined)
            unless block
              raise ArgumentError, "setting #{method_name}: no value and no block given"
            end
            self.config = config.with(method_name => block)
          else
            if block
              raise ArgumentError, "ambiguous invocation setting #{method_name}: give either a value or a block, not both."
            end
            self.config = config.with(method_name => arg)
          end
        end
      end
    end