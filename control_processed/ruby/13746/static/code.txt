def construct_request_hash
      request = {
        url: url,
        component: component,
        action: action,
        params: params,
        session: session,
        cgi_data: cgi_data,
        sanitizer: request_sanitizer
      }
      request.delete_if {|k,v| config.excluded_request_keys.include?(k) }
      Util::RequestPayload.build(request)
    end