def begin_change_vnet_as_lazy(resource_group_name, name, vnet_info, custom_headers:nil)
      response = begin_change_vnet_async(resource_group_name, name, vnet_info, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          begin_change_vnet_next_async(next_page_link, custom_headers:custom_headers)
        end
        page
      end
    end