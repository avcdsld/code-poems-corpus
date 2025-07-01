def list_capacities_next(next_page_link, custom_headers:nil)
      response = list_capacities_next_async(next_page_link, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end