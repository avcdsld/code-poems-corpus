def update
      @script_extension.user_id = current_user.id
      @script_extension.org_id = current_user.org_id
      if @script_extension.update(script_extension_params)
        redirect_to script_extensions_url, notice: 'Extension was successfully updated.'
        else
          render :edit
      end
    end