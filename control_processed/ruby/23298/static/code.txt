def coerce_property(property, options)
      unless options.is_a?(Hash)
        options = { class: options }
      end

      coercion_method = ->(obj) do
        if obj.respond_to?(:coerce)
          obj.method(:coerce)
        elsif obj.respond_to?(:new)
          obj.method(:new)
        else
          raise ArgumentError, "#{obj.inspect} does not implement neither .coerce nor .new"
        end
      end

      if options.has_key?(:collection)
        klass = options[:collection]
        coercion = ->(value) { value.map { |el| coercion_method[klass][el] } }
      elsif options.has_key?(:class)
        klass = options[:class]
        coercion = ->(value) { coercion_method[klass][value] }
      else
        raise ArgumentError, "You need to specify either :class or :collection"
      end

      coercions[property.to_s] = coercion
    end