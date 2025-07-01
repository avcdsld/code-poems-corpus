def manage
      @comments = current_user.comcoms.with_users.active.recent.page(params[:page])
      render comment_template(:manage)
    end