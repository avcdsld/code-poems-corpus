def render(*args)
      arguments(args) do
        assert_required ['text']
      end
      params = arguments.params
      params['raw'] = true

      post_request("markdown", arguments.params)
    end