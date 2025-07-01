def cd(url)
      new_uri = @uri.merge(url)
      if new_uri.host != @uri.host || new_uri.port != @uri.port || new_uri.scheme != @uri.scheme
        raise Exception , "uri must have same scheme, host and port"
      end
      @uri = new_uri
    end