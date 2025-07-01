def define_key _keycode, *args, &blk
      _symbol = @symbol
      h = $rb_prefix_map[_symbol]
      raise ArgumentError, "No such keymap #{_symbol} defined. Use define_prefix_command." unless h
      _keycode = _keycode[0].getbyte(0) if _keycode[0].class == String
      arg = args.shift
      if arg.is_a? String
        desc = arg
        arg = args.shift
      elsif arg.is_a? Symbol
        # its a symbol
        desc = arg.to_s
      elsif arg.nil?
        desc = "unknown"
      else
        raise ArgumentError, "Don't know how to handle #{arg.class} in PrefixManager"
      end
      @descriptions[_keycode] = desc

      if !block_given?
        blk = arg
      end
      h[_keycode] = blk
    end