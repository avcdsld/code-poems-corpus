def set_up_down_bars(params = {})
      # Map border to line.
      [:up, :down].each do |up_down|
        if params[up_down]
          params[up_down][:line] = params[up_down][:border] if params[up_down][:border]
        else
          params[up_down] = {}
        end
      end

      # Set the up and down bar properties.
      @up_down_bars = {
        :_up => Chartline.new(params[:up]),
        :_down => Chartline.new(params[:down])
      }
    end