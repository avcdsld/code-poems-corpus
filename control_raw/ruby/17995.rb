def stats(options = {})
      raise ArgumentError, '#stats requires a stats arg' unless options[:stats]
      raise ArgumentError, '#stats requires a group arg' unless options[:group]

      get '/stats', options
    end