def to_h
      self.class.fields.inject({}) do |h, (k, opts)|
        if opts[:as].nil?
          h[k] = self.public_send(k)
        else
          h[k] = self.public_send(opts[:as])
        end

        if !h[k].nil? && !h[k].is_a?(Array) && h[k].respond_to?(:to_h)
          h[k] = h[k].to_h
        end

        h
      end
    end