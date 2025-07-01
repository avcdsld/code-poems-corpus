def extract_slice_arguments(*args)
      offset, limit = case args.size
        when 2 then extract_offset_limit_from_two_arguments(*args)
        when 1 then extract_offset_limit_from_one_argument(*args)
      end

      return offset, limit if offset && limit

      raise ArgumentError, "arguments may be 1 or 2 Integers, or 1 Range object, was: #{args.inspect}"
    end