def reload
      reloaded = _reload
      if Mongoid.raise_not_found_error && reloaded.empty?
        raise Errors::DocumentNotFound.new(self.class, _id, _id)
      end
      @attributes = reloaded
      @attributes_before_type_cast = {}
      changed_attributes.clear
      reset_readonly
      apply_defaults
      reload_relations
      run_callbacks(:find) unless _find_callbacks.empty?
      run_callbacks(:initialize) unless _initialize_callbacks.empty?
      self
    end