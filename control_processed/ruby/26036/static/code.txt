def create
      user = Blogo::User.find_by_email(params[:email])
      if user && user.authenticate(params[:password])
        session[:blogo_user_id] = user.id
        redirect_to blogo_admin_url, notice: I18n.translate('blogo.admin.logged_in')
      else
        flash.now.alert = I18n.translate('blogo.admin.login_fail')
        render "new"
      end
    end