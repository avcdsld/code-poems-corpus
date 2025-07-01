def after_failure(*args, &block)
      options = (args.last.is_a?(Hash) ? args.pop : {})
      options[:do] = args if args.any?
      assert_valid_keys(options, :on, :do, :if, :unless)
      
      add_callback(:failure, options, &block)
    end