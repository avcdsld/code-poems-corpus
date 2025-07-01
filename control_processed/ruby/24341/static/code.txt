def index
      @channels = Channel.all

      respond_to do |format|
        format.html # index.html.erb
        format.json { render json: @channels }
      end
    end