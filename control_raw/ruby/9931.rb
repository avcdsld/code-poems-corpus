def list_source_controls_next(next_page_link, custom_headers:nil)
      response = list_source_controls_next_async(next_page_link, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end