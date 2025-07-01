def interactive_ssh(run=true)
      debug "interactive_ssh with keys: #{@rye_opts[:keys].inspect}"
      run = false unless STDIN.tty?
      args = []
      @rye_opts[:keys].each { |key| args.push *[:i, key] }
      args << "#{@rye_user}@#{@rye_host}"
      cmd = Rye.prepare_command("ssh", args)
      return cmd unless run
      system(cmd)
    end