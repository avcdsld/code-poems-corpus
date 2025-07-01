def set_target
        target_type = params[:target_type]
        if params[:target_id].blank? && params["#{target_type.to_resource_name}_id"].blank?
          target_class = target_type.to_model_class
          current_resource_method_name = "current_#{params[:devise_type].to_resource_name}"
          params[:target_id] = target_class.resolve_current_devise_target(send(current_resource_method_name))
          render(plain: "403 Forbidden: Unauthenticated as default target", status: 403) and return if params[:target_id].blank?
        end
        super
      end