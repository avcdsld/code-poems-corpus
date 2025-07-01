def option_as_array(option)
      value = Merb::Plugins.config[:exceptions][option]
      case value
      when Array
        value.reject { |e| e.nil? } # Don't accept nil values
      when String
        [value]
      else
        []
      end
    end