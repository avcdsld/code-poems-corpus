def list_by_users_as_lazy(resource_group_name, service_name, uid, filter:nil, top:nil, skip:nil, custom_headers:nil)
      response = list_by_users_async(resource_group_name, service_name, uid, filter:filter, top:top, skip:skip, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          list_by_users_next_async(next_page_link, custom_headers:custom_headers)
        end
        page
      end
    end