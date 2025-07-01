def topic(id, options={})
      params = { :lang => @query_options[:lang], :limit => @query_options[:limit] }.merge(options)
      get(surl('topic') + id, params, format: :json).parsed_response
    end