def instance_methods_eval(&block)
      raise ArgumentError, "block required" unless block_given?

      context = eval('self', block.binding)

      context.send :push_redirection_target, self

      begin
        yield context
      ensure
        context.send :pop_redirection_target
      end

      self
    end