def add_api_key(object, request_options = {}, max_queries_per_IP_per_hour = 0, max_hits_per_query = 0, indexes = nil)
      if object.instance_of?(Array)
        params = { :acl => object }
      else
        params = object
      end

      validity = 0
      unless request_options.is_a?(Hash)
        validity = request_options
        request_options = {}
      end

      params[:indexes] = indexes if indexes
      params['validity'] = validity.to_i if validity != 0
      params['maxHitsPerQuery'] = max_hits_per_query.to_i if max_hits_per_query != 0
      params['maxQueriesPerIPPerHour'] = max_queries_per_IP_per_hour.to_i if max_queries_per_IP_per_hour != 0

      post(Protocol.keys_uri, params.to_json, :write, request_options)
    end