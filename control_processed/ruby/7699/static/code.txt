def list_multi_role_pools_as_lazy(resource_group_name, name, custom_headers:nil)
      response = list_multi_role_pools_async(resource_group_name, name, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          list_multi_role_pools_next_async(next_page_link, custom_headers:custom_headers)
        end
        page
      end
    end