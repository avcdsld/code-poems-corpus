def cache_results(&block)
        return yield unless template_cache_configured? && defined?(@_cache_key)

        if cache_read_on_render?
          fetch_result_from_cache(cache_key, @_cache_options, &block)
        else
          write_result_to_cache(cache_key, @_cache_options, &block)
        end
      end