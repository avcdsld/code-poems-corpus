def call(schema = @schema, instance = @instance)
      schema.each do |schema_key, schema_value|
        if schema_value.is_a?(Hash)
          check_for_ar(schema, instance, schema_key, schema_value)
        else
          ValueAssigner.assign(Schema.new(schema_key, schema_value),
                               instance) { |coerced_value| schema[schema_key] = coerced_value }
        end
      end
    rescue NoMethodError => e
      Surrealist::ExceptionRaiser.raise_invalid_key!(e)
    end