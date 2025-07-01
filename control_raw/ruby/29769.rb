def assert_button_not_present(button_id)
      @web_browser.buttons.each { |button|
				the_button_id = RWebSpec.framework == "Watir" ? button.id : button["id"]	
        perform_assertion { assert(the_button_id != button_id, "unexpected button id: #{button_id} found") }
      }
    end