def create
      @script_extension = Script::Extension.new(script_extension_params)
      @script_extension.user_id = current_user.id
      @script_extension.org_id = current_user.org_id
      if @script_extension.save
        redirect_to script_extensions_url, notice: 'Extension was successfully created.'
        else
        render :new
      end
    end