def get(key, local = false)
      expanded_key = expand_key(key)

      if local && value = @fetch_cache.get(expanded_key)
        return value
      end

      value = @cache_wrapper.get(expanded_key)
      @fetch_cache.set(expanded_key, value) if local

      value
    end