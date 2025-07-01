def retrieve_payment(location_id, payment_id, opts = {})
      data, _status_code, _headers = retrieve_payment_with_http_info(location_id, payment_id, opts)
      return data
    end