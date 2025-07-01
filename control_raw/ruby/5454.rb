def to_redis_params
      { url: redis_url }.tap do |params|
        next if redis_sentinels.nil?

        raise ArgumentError, "redis_sentinels must be an array; got #{redis_sentinels}" unless
          redis_sentinels.is_a?(Array)

        next if redis_sentinels.empty?

        params[:sentinels] = redis_sentinels.map(&method(:parse_sentinel))
      end
    end