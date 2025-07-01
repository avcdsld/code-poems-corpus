def previous(params = {})
      query = Picture.ransack(params[:q])
      Picture.search_by(params, query).where("name < ?", name).last
    end