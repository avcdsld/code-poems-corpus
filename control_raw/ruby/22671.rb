def add_uri(force_update_mode, onerror_mode, uri)
      fmode = force_update_mode.nil?
      uri += '&forceUpdateMode=' + force_update_mode unless fmode
      uri += '&onErrorMode=' + onerror_mode unless onerror_mode.nil?
      uri
    end