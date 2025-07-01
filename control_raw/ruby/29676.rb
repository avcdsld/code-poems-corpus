def click_button_with_name(name, opts={})
      if opts && opts[:index]
        wait_before_and_after { button(:name => name, :index => opts[:index]).click }
      else
        wait_before_and_after { button(:name, name).click }
      end
    end