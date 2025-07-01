def begin_create_subscription_in_enrollment_account(enrollment_account_name, body, custom_headers:nil)
      response = begin_create_subscription_in_enrollment_account_async(enrollment_account_name, body, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end