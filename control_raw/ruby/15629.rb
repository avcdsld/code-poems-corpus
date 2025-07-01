def handle(*exceptions, &block)
      options = exceptions.last.is_a?(Hash) ? exceptions.pop : {}

      unless options.key?(:with)
        if block_given?
          options[:with] = block
        else
          raise ArgumentError, 'Need to provide error handler.'
        end
      end
      evaluate_exceptions(exceptions, options)
    end