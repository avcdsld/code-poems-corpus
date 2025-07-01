def help
      # We use the optionparser for this. Its just easier. We don't use
      # an optionparser above because I don't think the performance hits
      # of creating a whole object are worth checking only a couple flags.
      opts = OptionParser.new do |o|
        o.banner = "Usage: vagrant [options] <command> [<args>]"
        o.separator ""
        o.on("-v", "--version", "Print the version and exit.")
        o.on("-h", "--help", "Print this help.")
        o.separator ""
        o.separator "Common commands:"

        # Add the available subcommands as separators in order to print them
        # out as well.
        commands = {}
        longest = 0
        Vagrant.plugin("2").manager.commands.each do |key, data|
          # Skip non-primary commands. These only show up in extended
          # help output.
          next if !data[1][:primary]

          key           = key.to_s
          klass         = data[0].call
          commands[key] = klass.synopsis
          longest       = key.length if key.length > longest
        end

        commands.keys.sort.each do |key|
          o.separator "     #{key.ljust(longest+2)} #{commands[key]}"
          @env.ui.machine("cli-command", key.dup)
        end

        o.separator ""
        o.separator "For help on any individual command run `vagrant COMMAND -h`"
        o.separator ""
        o.separator "Additional subcommands are available, but are either more advanced"
        o.separator "or not commonly used. To see all subcommands, run the command"
        o.separator "`vagrant list-commands`."
      end

      @env.ui.info(opts.help, prefix: false)
    end