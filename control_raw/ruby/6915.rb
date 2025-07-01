def list_by_automation_account_next(next_page_link, custom_headers:nil)
      response = list_by_automation_account_next_async(next_page_link, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end