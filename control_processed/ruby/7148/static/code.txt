def list_by_replication_fabrics_as_lazy(fabric_name, custom_headers:nil)
      response = list_by_replication_fabrics_async(fabric_name, custom_headers:custom_headers).value!
      unless response.nil?
        page = response.body
        page.next_method = Proc.new do |next_page_link|
          list_by_replication_fabrics_next_async(next_page_link, custom_headers:custom_headers)
        end
        page
      end
    end