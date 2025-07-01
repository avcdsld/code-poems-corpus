def as_json(options=nil)
      return {} if messages.empty?
      attribute, types = messages.first
      type             = types.first

      {
        :error => {
          :param => attribute,
          :type  => type,
          :message => nil
        }
      }
    end