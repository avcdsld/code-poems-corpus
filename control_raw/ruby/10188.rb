def list_by_sync_group_as_lazy(resource_group_name, server_name, database_name, sync_group_name, custom_headers:nil)
      response = list_by_sync_group_async(resource_group_name, server_name, database_name, sync_group_name, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          list_by_sync_group_next_async(next_page_link, custom_headers:custom_headers)
        end
        page
      end
    end