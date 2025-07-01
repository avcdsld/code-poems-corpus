def process_action_link_action(render_action = :action_update, crud_type_or_security_options = nil)
      if request.get?
        # someone has disabled javascript, we have to show confirmation form first
        @record = find_if_allowed(params[:id], :read) if params[:id]
        respond_to_action(:action_confirmation)
      else
        @action_link = active_scaffold_config.action_links[action_name]
        if params[:id]
          crud_type_or_security_options ||= {:crud_type => request.post? || request.put? ? :update : :delete, :action => action_name}
          get_row(crud_type_or_security_options)
          if @record.nil?
            self.successful = false
            flash[:error] = as_(:no_authorization_for_action, :action => action_name)
          else
            yield @record
          end
        else
          yield
        end
        respond_to_action(render_action)
      end
    end