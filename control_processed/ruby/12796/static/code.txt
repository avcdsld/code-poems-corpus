def validate(type, plugin, attributes, attribute_namespace = [])
      attributes.each do |attribute|
        if attribute.children?
          validate(type, plugin, attribute.children, attribute_namespace.clone.push(attribute.name))
        elsif attribute.required? && attribute.value.nil?
          registry.logger.fatal I18n.t(
            "lita.config.missing_required_#{type}_attribute",
            type => plugin.namespace,
            attribute: full_attribute_name(attribute_namespace, attribute.name)
          )
          abort
        end
      end
    end