def count(&block)
      return keys.count unless block_given?
      proxy = HashProxy.new
      keys.inject(0) do |count, key|
        proxy.with(mapper[key], &block) ? count.succ : count
      end
    end