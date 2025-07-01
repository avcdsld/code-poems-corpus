def received(*args)
      arguments(args, required: [:user])
      params = arguments.params

      public_events = if params['public']
        params.delete('public')
        '/public'
      end

      response = get_request("/users/#{arguments.user}/received_events#{public_events}", params)
      return response unless block_given?
      response.each { |el| yield el }
    end