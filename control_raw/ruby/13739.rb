def shell(shell_type, shell_opts = {})
      shell = shell_factory.create_shell(shell_type, shell_opts)
      if block_given?
        begin
          yield shell
        ensure
          shell.close
        end
      else
        shell
      end
    end