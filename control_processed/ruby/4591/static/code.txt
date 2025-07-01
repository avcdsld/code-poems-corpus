def diff_from(ts = nil, version: nil, time: nil)
      Deprecations.show_ts_deprecation_for("#diff_from") if ts
      time ||= ts
      time = parse_time(time) if time
      changes = log_data.diff_from(time: time, version: version).tap do |v|
        deserialize_changes!(v)
      end

      changes.delete_if { |k, _v| deleted_column?(k) }

      { "id" => id, "changes" => changes }
    end