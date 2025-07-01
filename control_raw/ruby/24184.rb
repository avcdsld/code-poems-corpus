def renum(type_name, values = :defined_in_block, &block)
      nest = self.is_a?(Module) ? self : Object
      EnumeratedValueTypeFactory.create(nest, type_name, values, &block)
    end