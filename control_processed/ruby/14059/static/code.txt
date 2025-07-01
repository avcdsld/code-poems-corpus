def keep_description_and_icon_up_to_date=(new_val)
      return nil if new_val == @keep_description_and_icon_up_to_date
      raise JSS::InvalidDataError, 'New value must be true or false' unless new_val.jss_boolean?
      @keep_description_and_icon_up_to_date = new_val
      @need_to_update = true
    end