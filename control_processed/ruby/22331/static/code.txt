def destroy
      authentication = current_user.authentications.find_by(id: params[:id])
      authentication.destroy

      redirect_to authentications_path
    end