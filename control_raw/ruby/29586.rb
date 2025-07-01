def click_button_with_value(value, opts={})
        all_buttons = button_elements
        if opts && opts[:index]
          all_buttons.select{|x| x.attribute('value') == caption}[index]
        else
          all_buttons.each do |button|
            if button.attribute('value') == value then
              button.click
              return
            end
          end
        end
      end