def handle_resource(definition, parent, parent_params)
      if definition.is_a? Array
        return definition.each{|d| handle_resource(d, parent, parent_params)}
      end
      # normalize to a hash
      unless definition.is_a? Hash
        definition = {definition => nil}
      end

      definition.each do |name, child_definition|
        if !parent_params || !parent_params.has_key?(name.to_s)
          next
        end
        
        reflection = parent.class.reflect_on_association(name)
        
        attrs = parent_params.delete(name.to_s)

        if reflection.collection?
          attrs ||= []
          handle_plural_resource parent, name, attrs, child_definition
        else
          handle_singular_resource parent, name, attrs, child_definition
        end
      end
    end