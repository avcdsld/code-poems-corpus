def create_bucket(name, options = {})
      defaults = {
        :type => "couchbase",
        :ram_quota => 100,
        :replica_number => 1,
        :auth_type => "sasl",
        :sasl_password => "",
        :proxy_port => nil,
        :flush_enabled => false,
        :replica_index => true,
        :parallel_db_and_view_compaction => false
      }
      options = defaults.merge(options)
      params = {"name" => name}
      params["bucketType"] = options[:type]
      params["ramQuotaMB"] = options[:ram_quota]
      params["replicaNumber"] = options[:replica_number]
      params["authType"] = options[:auth_type]
      params["saslPassword"] = options[:sasl_password]
      params["proxyPort"] = options[:proxy_port]
      params["flushEnabled"] = options[:flush_enabled] ? 1 : 0
      params["replicaIndex"] = options[:replica_index] ? 1 : 0
      params["parallelDBAndViewCompaction"] = !!options[:parallel_db_and_view_compaction]
      payload = Utils.encode_params(params.reject! { |_k, v| v.nil? })
      response = @connection.send(:__http_query, :management, :post,
                                  "/pools/default/buckets", payload,
                                  "application/x-www-form-urlencoded", nil, nil, nil)
      Result.new(response.merge(:operation => :create_bucket))
    end