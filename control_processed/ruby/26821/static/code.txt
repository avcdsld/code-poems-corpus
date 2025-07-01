def accept
      @translation = Translation.find(params[:translation_id])
      @translation_already_accepted = @translation.key.accepted_in? session[:lang_to]
      @translation.accept
      respond_to do |format|
        format.js
      end
    end