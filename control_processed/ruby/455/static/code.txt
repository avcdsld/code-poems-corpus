def fetch_app_id
      return @apple_id if @apple_id
      config[:app_identifier] = fetch_app_identifier

      if config[:app_identifier]
        @app ||= Spaceship::Tunes::Application.find(config[:app_identifier])
        UI.user_error!("Couldn't find app '#{config[:app_identifier]}' on the account of '#{config[:username]}' on App Store Connect") unless @app
        app_id ||= @app.apple_id
      end

      app_id ||= UI.input("Could not automatically find the app ID, please enter it here (e.g. 956814360): ")

      return app_id
    end