def apply_fee(location_id, item_id, fee_id, opts = {})
      data, _status_code, _headers = apply_fee_with_http_info(location_id, item_id, fee_id, opts)
      return data
    end