def call(data = {}, options = {})
      m = options.delete(:method)
      client.call m || method, href_template, data, options
    end