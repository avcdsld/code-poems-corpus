def timestamp=(values)
      values.each do |value|
        case value
        when String, Symbol, TrueClass
          @timestamps << value
        else
          fail ArgumentError, 'timestamp must be either: true, a String or a Symbol'
        end
      end
    end