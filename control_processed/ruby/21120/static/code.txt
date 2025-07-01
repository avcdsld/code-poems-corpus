def call
      if requested_command && commands.has_key?(requested_command)
        self.command_method = commands[requested_command].method(:call)
      end

      command_method.call(_args.drop(1))

      self
    end