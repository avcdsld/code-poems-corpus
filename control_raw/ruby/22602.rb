def get_host(name)
      begin
        @host.get_host(name)
      rescue => ex
        Util.log_exception(ex, caller_locations(1, 1)[0].label)
        raise ex
      end
    end