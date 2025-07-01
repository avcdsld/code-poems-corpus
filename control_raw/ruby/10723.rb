def list_as_lazy(skiptoken:nil, skip:nil, top:nil, select:nil, search:nil, filter:nil, view:nil, group_name:nil, cache_control:'no-cache', custom_headers:nil)
      response = list_async(skiptoken:skiptoken, skip:skip, top:top, select:select, search:search, filter:filter, view:view, group_name:group_name, cache_control:cache_control, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          list_next_async(next_page_link, cache_control:cache_control, custom_headers:custom_headers)
        end
        page
      end
    end