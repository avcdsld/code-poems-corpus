def method_missing(*args, &block)
      # Get the configuration
      if args.last.is_a?(Hash)
        options = args.last
      else
        args << options = {}
      end
      
      # Get any existing condition that may need to be merged
      if_condition = options.delete(:if)
      unless_condition = options.delete(:unless)
      
      # Provide scope access to configuration in case the block is evaluated
      # within the object instance
      proxy = self
      proxy_condition = @condition
      
      # Replace the configuration condition with the one configured for this
      # proxy, merging together any existing conditions
      options[:if] = lambda do |*condition_args|
        # Block may be executed within the context of the actual object, so
        # it'll either be the first argument or the executing context
        object = condition_args.first || self
        
        proxy.evaluate_method(object, proxy_condition) &&
        Array(if_condition).all? {|condition| proxy.evaluate_method(object, condition)} &&
        !Array(unless_condition).any? {|condition| proxy.evaluate_method(object, condition)}
      end
      
      # Evaluate the method on the owner class with the condition proxied
      # through
      machine.owner_class.send(*args, &block)
    end