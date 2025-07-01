def to_hash
      attributes.inject({}) do |hash, (key, value)|
        unless Resource::Base.has_attribute?(key)
          hash[Util.camelize(key, true)] = send(key.to_sym)
        end

        hash
      end
    end