def expired?(service_name)
      if entry = @record_cache[service_name]
        return Time.now > (entry.resolution_time + entry.ttl)
      else
        return true
      end
    end