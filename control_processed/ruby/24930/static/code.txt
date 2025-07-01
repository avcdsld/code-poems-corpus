def check_arguments arguments
        arguments.each_with_index do |argument, index|
          next if argument.is_a? Numeric
          next if argument.is_a? String
          next if argument.is_a? Symbol
          next if argument.is_a? Hash
          next if argument.is_a? NilClass
          next if argument.is_a? TrueClass
          next if argument.is_a? FalseClass

          raise ArgumentError, "Cannot send complex data for block argument #{index + 1}: #{argument.class.name}"
        end

        arguments
      end