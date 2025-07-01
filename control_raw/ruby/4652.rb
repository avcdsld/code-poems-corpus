def update(*args)
      arguments(args, required: [:card_id])
      params = arguments.params

      params["accept"] ||= ::Github::Client::Projects::PREVIEW_MEDIA

      patch_request("/projects/columns/cards/#{arguments.card_id}", params)
    end