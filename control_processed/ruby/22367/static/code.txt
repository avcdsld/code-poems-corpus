def create
      group = Group.find_by(id: membership_params[:group_id])

      Group::Services::Join.new(group: group, person: current_user).call

      redirect_to group
    end