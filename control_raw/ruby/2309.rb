def repl
      until @proceed
        cmd = interface.read_command(prompt)
        return if cmd.nil?

        next if cmd == ""

        run_cmd(cmd)
      end
    end