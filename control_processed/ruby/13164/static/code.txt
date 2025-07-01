def nested
      @page = Page.find_by(id: params[:page_id]) || Language.current_root_page

      render json: PageTreeSerializer.new(@page,
        ability: current_ability,
        user: current_alchemy_user,
        elements: params[:elements],
        full: true)
    end