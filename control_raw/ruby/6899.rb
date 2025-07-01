def list_as_lazy(reported_start_time, reported_end_time, show_details:nil, aggregation_granularity:nil, continuation_token:nil, custom_headers:nil)
      response = list_async(reported_start_time, reported_end_time, show_details:show_details, aggregation_granularity:aggregation_granularity, continuation_token:continuation_token, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          list_next_async(next_page_link, custom_headers:custom_headers)
        end
        page
      end
    end