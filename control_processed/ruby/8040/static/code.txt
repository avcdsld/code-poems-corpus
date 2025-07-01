def list_site_analyses_as_lazy(resource_group_name, site_name, diagnostic_category, custom_headers:nil)
      response = list_site_analyses_async(resource_group_name, site_name, diagnostic_category, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          list_site_analyses_next_async(next_page_link, custom_headers:custom_headers)
        end
        page
      end
    end