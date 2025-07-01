def connection(api, options = {})
      connection_options = default_options(options)
      connection_options.merge!(builder: stack(options.merge!(api: api)))
      if options[:connection_options]
        connection_options.deep_merge!(options[:connection_options])
      end
      if ENV['DEBUG']
        p "Connection options : \n"
        pp connection_options
      end
      Faraday.new(connection_options)
    end