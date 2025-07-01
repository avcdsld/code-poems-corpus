def create
      @script_listing = Script::Listing.find(params[:listing_id])
      @script_url = @script_listing.urls.create(script_url_params)
      @script_url.user_id = current_user.id
      @script_url.org_id = current_user.org_id
      if @script_url.save
        redirect_to script_listing_urls_path, notice: 'Author was successfully created.'
        else
          render :new
      end
    end