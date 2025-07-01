def valid!(original, sanitized, fallback = nil, options = {})
      return sanitized unless sanitized.nil?
      unless original.nil?
        raise ValidationError, options[:invalid_error] % original.inspect
      end
      return instance_variable_get(fallback) if fallback_exist?(fallback)
      return yield if block_given?
      raise ValidationError, options[:required_error] if options[:required]
    end