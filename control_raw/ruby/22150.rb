def go(argv, opts, config)
      opts.banner = "Usage: #{syntax}"
      process_options(opts, config)
      add_default_options(opts)

      if argv[0] && cmd = commands[argv[0].to_sym]
        logger.debug "Found subcommand '#{cmd.name}'"
        argv.shift
        cmd.go(argv, opts, config)
      else
        logger.debug "No additional command found, time to exec"
        self
      end
    end