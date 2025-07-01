def plugin_class(options = {})
      options = { fail_gracefully: false }.merge(options)

      const = _plugin_constant
      fail TypeError, "no constant: #{_constant_name}" unless const
      @plugin_class ||= Guard.const_get(const)

    rescue TypeError
      begin
        require "guard/#{ name.downcase }"
        const = _plugin_constant
        @plugin_class ||= Guard.const_get(const)

      rescue TypeError => error
        UI.error "Could not find class Guard::#{ _constant_name }"
        UI.error error.backtrace.join("\n")
        # TODO: return value or move exception higher
      rescue LoadError => error
        unless options[:fail_gracefully]
          msg = format(ERROR_NO_GUARD_OR_CLASS, name.downcase, _constant_name)
          UI.error(msg)
          UI.error("Error is: #{error}")
          UI.error(error.backtrace.join("\n"))
          # TODO: return value or move exception higher
        end
      end
    end