def add_request_headers(request)
      log.info "Adding request headers..."

      headers = {
        'Accept'         => 'application/json',
        'Content-Type'   => 'application/json',
        'Connection'     => 'keep-alive',
        'Keep-Alive'     => '30',
        'User-Agent'     => user_agent,
        'X-Chef-Version' => '11.4.0',
      }

      headers.each do |key, value|
        log.debug "#{key}: #{value}"
        request[key] = value
      end
    end