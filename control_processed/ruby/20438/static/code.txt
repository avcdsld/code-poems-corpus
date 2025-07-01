def copy(url, destination, options = {})
      connection(url, options) do |uri, conn|
        conn.copy(uri.request_uri, destination, options)
      end
    end