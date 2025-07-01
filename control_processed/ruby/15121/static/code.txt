def add_headers(request)
      return if Logging.correlation_id.nil?
      request.add_field(CLIENT_REQUEST_ID.to_s, Logging.correlation_id)
      request.add_field(CLIENT_RETURN_CLIENT_REQUEST_ID.to_s, true)
    end