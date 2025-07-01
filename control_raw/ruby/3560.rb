def json_response(response_code, data, options = {})
      options = { pretty: true }.merge(options)
      do_pretty_json = !!options.delete(:pretty) # make sure we have a proper Boolean.
      json = FFI_Yajl::Encoder.encode(data, pretty: do_pretty_json)
      already_json_response(response_code, json, options)
    end