def image(name,locator)

        # generates method for checking the existence of the image.
        # this will return true or false based on if image is available or not
        # @example check if 'logo' image is displayed on the page
        # text(:logo,"xpath~//UITextField")
        # DSL for clicking the logo image.
        # def click_logo
        #  logo # This will click on the logo text on the screen.
        # end
        define_method("#{name}?") do
          ScreenObject::AppElements::Image.new(locator).exists?
        end

        #generates method for clicking image
        # this will not return any value.
        # @example clicking on logo image.
        # text(:logo,"xpath~//UITextField")
        # DSL for clicking the logo image.
        # def click_logo
        #  logo # This will click on the logo text on the screen.
        # end
        define_method("#{name}") do
          ScreenObject::AppElements::Image.new(locator).click
        end
      end