def object
      instance_variable_defined?(:@object) ? @object : @object = begin
        if media_type == 'application/json'
          JSON.parse(body) rescue nil
        elsif media_type == 'application/x-www-form-urlencoded'
          CGI.parse(body).map { |k, vs| {k => vs.last} }.inject({}, &:update)
        end
      end
    end