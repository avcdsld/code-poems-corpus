def window_opened_by(**options)
      old_handles = driver.window_handles
      yield

      synchronize_windows(options) do
        opened_handles = (driver.window_handles - old_handles)
        if opened_handles.size != 1
          raise Capybara::WindowError, 'block passed to #window_opened_by '\
                                       "opened #{opened_handles.size} windows instead of 1"
        end
        Window.new(self, opened_handles.first)
      end
    end