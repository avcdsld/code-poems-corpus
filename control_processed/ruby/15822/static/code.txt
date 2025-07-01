def dial(session_id, token, sip_uri, opts)
      response = @client.dial(session_id, token, sip_uri, opts)
    end