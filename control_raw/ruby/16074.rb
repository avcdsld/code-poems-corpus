def with_shard(shard)
      shard = cluster.to_shard(shard)

      old_shard = current_shard
      old_fixed = fixed_shard
      self.current_shard = shard
      self.fixed_shard = shard
      yield
    ensure
      self.fixed_shard = old_fixed
      self.current_shard = old_shard
    end