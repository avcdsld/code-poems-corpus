def option(*args, &block)
      switches, description = Runner.separate_switches_from_description(*args)
      proc = block || option_proc(switches)
      @options << {
        args: args,
        proc: proc,
        switches: switches,
        description: description,
      }
    end