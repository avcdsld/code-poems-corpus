def add_command(command=nil,&block)
      command = Commands::Command.new(&block) if block_given?
      current_connection.add_command(command)
    end