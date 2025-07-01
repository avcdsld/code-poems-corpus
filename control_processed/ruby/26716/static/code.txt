def new
      @script_licence = Script::Licence.new
      @script_licence.user_id = current_user.id
      @script_licence.org_id = current_user.org_id
    end