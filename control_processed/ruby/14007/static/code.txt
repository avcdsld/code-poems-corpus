def validate_package_opts(identifier, opts)
      opts[:position] ||= -1
      opts[:action] ||= :install
      opts[:feu] ||= false
      opts[:fut] ||= false
      opts[:update_autorun] ||= false

      opts[:position] =
        case opts[:position]
        when :start then 0
        when :end then -1
        else JSS::Validate.integer(opts[:position])
        end

      # if the given position is past the end, set it to -1 (the end)
      opts[:position] = -1 if opts[:position] > @packages.size

      id = JSS::Package.valid_id identifier, api: @api

      raise JSS::NoSuchItemError, "No package matches '#{identifier}'" unless id

      raise JSS::InvalidDataError, "action must be one of: :#{PACKAGE_ACTIONS.keys.join ', :'}" unless \
        PACKAGE_ACTIONS.include? opts[:action]

      opts[:feu] = JSS::Validate.boolean opts[:feu]
      opts[:fut] = JSS::Validate.boolean opts[:fut]
      opts[:update_autorun] = JSS::Validate.boolean opts[:update_autorun]
      id
    end