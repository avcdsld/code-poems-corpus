def create(*args)
      arguments(args, required: [:column_id])
      params = arguments.params

      params["accept"] ||= ::Github::Client::Projects::PREVIEW_MEDIA

      post_request("/projects/columns/#{arguments.column_id}/cards", params)
    end