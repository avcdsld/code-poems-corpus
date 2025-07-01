def list_events_as_lazy(resource_group_name, registry_name, webhook_name, custom_headers:nil)
      response = list_events_async(resource_group_name, registry_name, webhook_name, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          list_events_next_async(next_page_link, custom_headers:custom_headers)
        end
        page
      end
    end