def get_transaction_by_id(budget_id, transaction_id, opts = {})
      data, _status_code, _headers = get_transaction_by_id_with_http_info(budget_id, transaction_id, opts)
      data
    end