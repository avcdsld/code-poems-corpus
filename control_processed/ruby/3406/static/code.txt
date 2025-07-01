def renew_token(client_id, body, opts = {})
      data, _status_code, _headers = renew_token_with_http_info(client_id, body, opts)
      return data
    end