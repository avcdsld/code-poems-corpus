def process_arg_val(arg, val, hsh, is_default = false)
            if is_default && arg.required? && (val.nil? || val.empty?)
                self.errors << "No value was specified for required argument '#{arg}'"
                return
            end
            if !is_default && val.nil? && KeywordArgument === arg
                if arg.value_optional?
                    val = arg.value_optional
                else
                    self.errors << "No value was specified for keyword argument '#{arg}'"
                    return
                end
            end

            # Argument value validation
            if ValueArgument === arg && arg.validation && val
                case arg.validation
                when Regexp
                    [val].flatten.each do |v|
                        add_value_error(arg, val) unless v =~ arg.validation
                    end
                when Array
                    [val].flatten.each do |v|
                        add_value_error(arg, val) unless arg.validation.include?(v)
                    end
                when Proc
                    begin
                        arg.validation.call(val, arg, hsh)
                    rescue StandardError => ex
                        self.errors << "An error occurred in the validation handler for argument '#{arg}': #{ex}"
                        return
                    end
                else
                    raise "Unknown validation type: #{arg.validation.class.name}"
                end
            end

            # TODO: Argument value coercion

            # Call any registered on_parse handler
            begin
                val = arg.on_parse.call(val, arg, hsh) if val && arg.on_parse
            rescue StandardError => ex
                self.errors << "An error occurred in the on_parse handler for argument '#{arg}': #{ex}"
                return
            end

            # Return result
            val
        end