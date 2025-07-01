def call_enum(name, other, enum)
      if other.is_a?(Vips::Image)
        Vips::Operation.call name.to_s, [self, other, enum]
      else
        Vips::Operation.call name.to_s + "_const", [self, enum, other]
      end
    end