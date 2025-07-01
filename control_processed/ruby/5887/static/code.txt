def additional_set_taxonomy
      params[:organization_id], original = find_organization(:owner).id, params[:organization_id] if params[:owner].present?
      set_taxonomy
      params[:organization_id] = original if params[:owner].present?
    end