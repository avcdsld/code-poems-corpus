def permitted_to? (privilege, object_or_sym = nil, options = {})
      if authorization_engine.permit!(privilege, options_for_permit(object_or_sym, options, false))
        yield if block_given?
        true
      else
        false
      end
    end