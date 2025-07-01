def get_balances_by_billing_account(billing_account_id, custom_headers:nil)
      response = get_balances_by_billing_account_async(billing_account_id, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end