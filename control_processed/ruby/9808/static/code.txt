def list_at_subscription_next(next_page_link, custom_headers:nil)
      response = list_at_subscription_next_async(next_page_link, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end