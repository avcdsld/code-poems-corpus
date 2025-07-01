def new_session
      app = Rails.application
      session = ActionDispatch::Integration::Session.new(app)
      yield session if block_given?

      # This makes app.url_for and app.foo_path available in the console
      session.extend(app.routes.url_helpers)
      session.extend(app.routes.mounted_helpers)

      session
    end