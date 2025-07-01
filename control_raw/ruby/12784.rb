def has_any_role_with_hierarchy?(*roles, &block)
      user_roles = authorization_engine.roles_with_hierarchy_for(current_user)
      result = roles.any? do |role|
        user_roles.include?(role)
      end
      yield if result and block_given?
      result
    end