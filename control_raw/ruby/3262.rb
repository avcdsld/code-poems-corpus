def delete_timecard(timecard_id, opts = {})
      data, _status_code, _headers = delete_timecard_with_http_info(timecard_id, opts)
      return data
    end