def list_app_service_plans_as_lazy(resource_group_name, name, custom_headers:nil)
      response = list_app_service_plans_async(resource_group_name, name, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          list_app_service_plans_next_async(next_page_link, custom_headers:custom_headers)
        end
        page
      end
    end