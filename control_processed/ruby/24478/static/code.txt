def and_yield(*args)
      yield eval_context = Object.new if block_given?
      @plan = Proc.new do |&block|
        eval_context.instance_exec(*args, &block)
      end
      self
    end