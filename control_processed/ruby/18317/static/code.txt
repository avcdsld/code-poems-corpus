def gifs_random_get(api_key, opts = {})
      data, _status_code, _headers = gifs_random_get_with_http_info(api_key, opts)
      return data
    end