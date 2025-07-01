def get_async_doc_status(id, opts = {})
      data, _status_code, _headers = get_async_doc_status_with_http_info(id, opts)
      return data
    end