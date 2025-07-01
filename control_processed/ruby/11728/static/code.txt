def node(n, options = {})
      custom_params = []
      custom_params << use_named_parameter('dc', options[:dc]) if options[:dc]

      ret = send_get_request(@conn, ["/v1/health/node/#{n}"], options, custom_params)
      JSON.parse(ret.body).map { |node| OpenStruct.new node }
    end