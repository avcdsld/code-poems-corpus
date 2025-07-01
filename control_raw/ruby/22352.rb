def create
      circle = Circle.find_by(id: tie_params[:circle_id])
      tie = circle.add_contact(tie_params[:contact_id])

      flash[:notice] = flash_message(action: :create, tie: tie, circle: circle)
      respond_to do |format|
        # format.html { redirect_to circle }
        format.js
      end
    end