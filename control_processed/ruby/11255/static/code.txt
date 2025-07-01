def list_current_by_database_as_lazy(resource_group_name, server_name, database_name, filter:nil, custom_headers:nil)
      response = list_current_by_database_async(resource_group_name, server_name, database_name, filter:filter, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          list_current_by_database_next_async(next_page_link, custom_headers:custom_headers)
        end
        page
      end
    end