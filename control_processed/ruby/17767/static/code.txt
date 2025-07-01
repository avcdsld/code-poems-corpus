def check_authorization
        unless current_user
          render nothing: true, status: :unauthorized
          return false
        end
        if params[:organization_id] && !parent_organization
          render nothing: true, status: :forbidden
          return false
        end
        true
      end