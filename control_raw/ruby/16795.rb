def json_for_query(calendar_ids, start_time, end_time)
      {}.tap{ |obj|
        obj[:items] = calendar_ids.map {|id| Hash[:id, id] }
        obj[:timeMin] = start_time.utc.iso8601
        obj[:timeMax] = end_time.utc.iso8601
      }.to_json
    end