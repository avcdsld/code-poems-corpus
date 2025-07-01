def validates_attachment_content_type name, options = {}
      validation_options = options.dup
      allowed_types = [validation_options[:content_type]].flatten
      validates_each(:"#{name}_content_type", validation_options) do |record, attr, value|
        if !allowed_types.any?{|t| t === value } && !(value.nil? || value.blank?)
          if record.errors.method(:add).arity == -2
            message = options[:message] || "is not one of #{allowed_types.join(", ")}"
            record.errors.add(:"#{name}_content_type", message)
          else
            record.errors.add(:"#{name}_content_type", :inclusion, :default => options[:message], :value => value)
          end
        end
      end
    end