def to_h
      {
        runtime_guid: tracer.guid,
        span_guid: context.id,
        trace_guid: context.trace_id,
        span_name: operation_name,
        attributes: tags.map {|key, value|
          {Key: key.to_s, Value: value}
        },
        oldest_micros: start_micros,
        youngest_micros: end_micros,
        error_flag: false,
        dropped_logs: dropped_logs_count,
        log_records: log_records
      }
    end