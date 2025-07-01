def rebase(upstream, opts = {})
      args = []
      if opts[:interactive]
        logger.info { "Interactively rebasing #{branches.current.name} against #{upstream}" }
        args << '-i'
        args << upstream
      elsif opts[:oldbase]
        logger.info { "Doing rebase from #{opts[:oldbase]} against #{upstream} on #{branches.current.name}" }
        args << '--onto' << upstream << opts[:oldbase] << branches.current.name
      else
        logger.info { "Rebasing #{branches.current.name} against #{upstream}" }
        args << upstream
      end
      return command('rebase', args)
    end