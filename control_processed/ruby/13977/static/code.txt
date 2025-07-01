def scope= (new_scope)
      raise JSS::InvalidDataError, "JSS::Scopable::Scope instance required" unless new_criteria.kind_of?(JSS::Scopable::Scope)
      raise JSS::InvalidDataError, "Scope object must have target_key of :#{self.class::SCOPE_TARGET_KEY}" unless self.class::SCOPE_TARGET_KEY == new_scope.target_key
      @scope = new_scope
      @need_to_update = true
    end