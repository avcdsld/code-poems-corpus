def write_error_bars(error_bars)
      return unless ptrue?(error_bars)

      if error_bars[:_x_error_bars]
        write_err_bars('x', error_bars[:_x_error_bars])
      end
      if error_bars[:_y_error_bars]
        write_err_bars('y', error_bars[:_y_error_bars])
      end
    end