def feature(name = nil)
      if !name
        self.class.features.keys
      else
        if self.class.features.key?(name)
          self.class.features[name]
        else
          fail "Feature #{name} does not exist!"
        end
      end
    end