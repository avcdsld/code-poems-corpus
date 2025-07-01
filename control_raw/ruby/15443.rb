def post(path, obj, params = {}, headers = {}, auth = true)
      request(http_method: :post, path: path, body: obj, query: params, headers: headers, auth: auth)
    end