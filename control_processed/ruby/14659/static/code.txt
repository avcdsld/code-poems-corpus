def parse!(args)
      do_parse(args)
    rescue OptionParser::InvalidOption => ex
      @exception_handler.call("Unknown option #{ex.args.join(' ')}",@extra_error_context)
    rescue OptionParser::InvalidArgument => ex
      @exception_handler.call("#{ex.reason}: #{ex.args.join(' ')}",@extra_error_context)
    end