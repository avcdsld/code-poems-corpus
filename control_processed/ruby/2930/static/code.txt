def find_attribute_value(tree, path, default)
      attribute = tree[path.shift]
      if attribute.is_a?(Hash)
        find_attribute_value(attribute, path, default)
      else
        attribute.nil? ? default : attribute
      end
    end