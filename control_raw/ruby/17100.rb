def session_key
      Rails.application.config.session_options.merge(request.session_options || {})[:key] ||
        ActionDispatch::Session::AbstractStore::DEFAULT_OPTIONS[:key]
    end