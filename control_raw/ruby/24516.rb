def prepend_to_file(relative_path, *args, **options, &block)
      log_status(:prepend, relative_path, options.fetch(:verbose, true),
                                          options.fetch(:color, :green))
      options.merge!(before: /\A/, verbose: false)
      inject_into_file(relative_path, *(args << options), &block)
    end