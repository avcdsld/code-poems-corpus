def fetch(options)
      timestamps = build_timestamps(options)
      params = { T: timestamps.join(","), c: nil }
      query(params)
    end