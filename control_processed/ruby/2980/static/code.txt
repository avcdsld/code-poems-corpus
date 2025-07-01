def elements(name, tag=:element, identifier={:index => 0}, &block)
      #
      # sets tag as element if not defined
      #
      if tag.is_a?(Hash)
        identifier = tag
        tag        = :element
      end

      define_method("#{name}_elements") do
        return call_block(&block) if block_given?
        platform.elements_for(tag, identifier.clone)
      end
    end