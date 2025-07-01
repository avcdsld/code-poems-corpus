def create(key, value, options = {})
      if key? key
        false
      else
        store(key, value, options)
        true
      end
    end