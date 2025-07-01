def securable
    Settings.new(metadata.merge(
                    settings:    raw_data,
                    pre_filters: [Filters::SecureFilter],
    ))
  end