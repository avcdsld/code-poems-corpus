def create
      @tag = Tag.new(params[:tag])

      respond_to do |format|
        if @tag.save
          format.html { redirect_to @tag, notice: 'Tag was successfully created.' }
          format.json { render json: @tag, status: :created, location: @tag }
        else
          format.html { render action: "new" }
          format.json { render json: @tag.errors, status: :unprocessable_entity }
        end
      end
    end