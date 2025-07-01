def update_timecard(timecard_id, body, opts = {})
      data, _status_code, _headers = update_timecard_with_http_info(timecard_id, body, opts)
      return data
    end