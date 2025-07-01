def create(klass, author, params, extra_log_info = {})
      perform_action!(:create, klass, author, extra_log_info) do
        klass.create(params)
      end
    end