def list_categories(location_id, opts = {})
      data, _status_code, _headers = list_categories_with_http_info(location_id, opts)
      return data
    end