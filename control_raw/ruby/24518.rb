def append_to_file(relative_path, *args, **options, &block)
      log_status(:append, relative_path, options.fetch(:verbose, true),
                                         options.fetch(:color, :green))
      options.merge!(after: /\z/, verbose: false)
      inject_into_file(relative_path, *(args << options), &block)
    end