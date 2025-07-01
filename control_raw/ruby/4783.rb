def to_hash(options = {})
      out = {}
      each_key do |k|
        assignment_key =
          if options[:stringify_keys]
            k.to_s
          elsif options[:symbolize_keys]
            k.to_s.to_sym
          else
            k
          end
        if self[k].is_a?(Array)
          out[assignment_key] ||= []
          self[k].each do |array_object|
            out[assignment_key] << maybe_convert_to_hash(array_object, options)
          end
        else
          out[assignment_key] = maybe_convert_to_hash(self[k], options)
        end
      end
      out
    end