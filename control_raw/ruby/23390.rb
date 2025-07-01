def enter
      if current_item.name == '.'  # do nothing
      elsif current_item.name == '..'
        cd '..'
      elsif in_zip?
        v
      elsif current_item.directory? || current_item.zip?
        cd current_item
      else
        v
      end
    end