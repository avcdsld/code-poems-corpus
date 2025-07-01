def mget(msg_id, keys)
      keys = keys.map{|suffix| key(msg_id, suffix)}
      with_failover { redis.mget(*keys) }
    end