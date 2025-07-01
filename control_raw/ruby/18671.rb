def hashify(*args, &block)
      key_value_pairs = args.map {|a| yield(a) }

      # if using Ruby 1.9,
      #   Hash[ key_value_pairs ]
      # is all that's needed, but for Ruby 1.8 compatability, these must
      # be flattened and the resulting array unpacked. flatten(1) only
      # flattens the arrays constructed in the block, it won't mess up
      # any values (or keys) that are themselves arrays/hashes.
      Hash[ *( key_value_pairs.flatten(1) )]
    end