def list_linked_databases_as_lazy(resource_group_name, server_name, sync_agent_name, custom_headers:nil)
      response = list_linked_databases_async(resource_group_name, server_name, sync_agent_name, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          list_linked_databases_next_async(next_page_link, custom_headers:custom_headers)
        end
        page
      end
    end