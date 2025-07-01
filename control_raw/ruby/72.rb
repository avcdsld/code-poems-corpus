def restore_attribute!(attr_name)
        attr_name = attr_name.to_s
        if attribute_changed?(attr_name)
          __send__("#{attr_name}=", attribute_was(attr_name))
          clear_attribute_change(attr_name)
        end
      end