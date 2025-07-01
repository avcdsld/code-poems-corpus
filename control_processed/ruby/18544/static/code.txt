def logout_method(user = current_user)
      http_method = security.logout_method
      http_method || if defined? ::Devise
                       scope = ::Devise::Mapping.find_scope! user
                       mapping = ::Devise.mappings[scope]
                       mapping.sign_out_via
                     end
    end