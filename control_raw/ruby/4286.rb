def field_names(options)
      names = (as_attributes.keys + attribute_names).uniq.sort

      only = Array.wrap(options[:only]).map(&:to_s)
      except = Array.wrap(options[:except]).map(&:to_s)
      except |= ['_type'] unless Mongoid.include_type_for_serialization

      if !only.empty?
        names &= only
      elsif !except.empty?
        names -= except
      end
      names
    end