def logout_path(user = current_user, app = main_app)
      path = security.logout_path
      path ||=
        if defined? ::Devise
          scope = ::Devise::Mapping.find_scope! user
          "destroy_#{scope}_session_path"
        end
      ModuleUtils.try_to app, path
    end