def add_class(parent_ref)
      klass = Klass.new(id_generator.call, parent_ref)
      @classes_by_id[klass.id] = klass
      klass
    end