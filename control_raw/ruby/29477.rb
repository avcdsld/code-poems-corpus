def get_request(slug, params={})
      # calls connection method on the extended module
      connection.get do |req|
        req.url "api/#{slug}"
        params.each_pair do |k,v|
          req.params[k] = v
        end
      end
    end