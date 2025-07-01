def list_timecard_events(timecard_id, opts = {})
      data, _status_code, _headers = list_timecard_events_with_http_info(timecard_id, opts)
      return data
    end