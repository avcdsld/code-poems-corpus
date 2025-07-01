def get_payee_by_id(budget_id, payee_id, opts = {})
      data, _status_code, _headers = get_payee_by_id_with_http_info(budget_id, payee_id, opts)
      data
    end