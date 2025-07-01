def get_volume_set(name)
      begin
        @volume_set.get_volume_set(name)
      rescue => ex
        Util.log_exception(ex, caller_locations(1, 1)[0].label)
        raise ex
      end
    end