def get_scheduled_transactions(budget_id, opts = {})
      data, _status_code, _headers = get_scheduled_transactions_with_http_info(budget_id, opts)
      data
    end