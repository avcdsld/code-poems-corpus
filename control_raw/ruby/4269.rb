def attribute_change(attr)
      attr = database_field_name(attr)
      [changed_attributes[attr], attributes[attr]] if attribute_changed?(attr)
    end