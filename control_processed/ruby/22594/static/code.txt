def get_vlun(volume_name)
      begin
        @vlun.get_vlun(volume_name)
      rescue => ex
        Util.log_exception(ex, caller_locations(1, 1)[0].label)
        raise ex
      end
    end