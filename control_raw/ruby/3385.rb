def list_settlements(location_id, opts = {})
      data, _status_code, _headers = list_settlements_with_http_info(location_id, opts)
      return data
    end