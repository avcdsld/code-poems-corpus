def list(reported_start_time, reported_end_time, show_details:nil, aggregation_granularity:nil, continuation_token:nil, custom_headers:nil)
      first_page = list_as_lazy(reported_start_time, reported_end_time, show_details:show_details, aggregation_granularity:aggregation_granularity, continuation_token:continuation_token, custom_headers:custom_headers)
      first_page.get_all_items
    end