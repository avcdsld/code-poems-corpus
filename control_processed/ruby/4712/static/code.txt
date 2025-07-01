def create(*args)
      arguments(args, required: [:user, :repo]) do
        permit VALID_DEPLOYMENTS_OPTIONS
        assert_required %w[ ref ]
      end
      params = arguments.params
      params['accept'] ||= PREVIEW_MEDIA

      post_request("repos/#{arguments.user}/#{arguments.repo}/deployments", arguments.params)
    end