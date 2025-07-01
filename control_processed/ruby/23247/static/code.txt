def lookup_service(service)
      code, message, uri = @proxy.lookupService(@caller_id, service)
      if code == 1
        uri
      else
        false
      end
    end