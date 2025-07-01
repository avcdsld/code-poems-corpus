def method_missing(method, *args, &block)
      clear_query_cache_if_needed(method)
      if shard_fixed?
        connection.send(method, *args, &block)
      elsif mixable?(method, *args)
        fader = @mixer.build_fader(method, *args, &block)
        logger.debug {
          "[ActiveRecord::Turntable] Sending method: #{method}, " \
          "sql: #{args.first}, " \
          "shards: #{fader.shards_query_hash.keys.map(&:name)}"
        }
        fader.execute
      else
        connection.send(method, *args, &block)
      end
    end