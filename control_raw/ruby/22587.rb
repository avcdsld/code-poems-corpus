def delete_flash_cache
      begin
        @flash_cache.delete_flash_cache
      rescue => ex
        Util.log_exception(ex, caller_locations(1, 1)[0].label)
        raise ex
      end
    end