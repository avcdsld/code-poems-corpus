def get_nodes_event_list(start_time_utc, end_time_utc, timeout:60, events_types_filter:nil, exclude_analysis_events:nil, skip_correlation_lookup:nil, custom_headers:nil)
      response = get_nodes_event_list_async(start_time_utc, end_time_utc, timeout:timeout, events_types_filter:events_types_filter, exclude_analysis_events:exclude_analysis_events, skip_correlation_lookup:skip_correlation_lookup, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end