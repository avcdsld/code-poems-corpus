def require_access!(resource, operation = nil)
      operation ||= current_operation
      ability_from_token.access!(resource.resource_class, operation)
    end