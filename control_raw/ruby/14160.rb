def validate_init_for_creation(args)
      raise JSS::UnsupportedError, "Creating #{self.class::RSRC_LIST_KEY} isn't yet supported. Please use other Casper workflows." unless creatable?

      raise JSS::MissingDataError, "You must provide a :name to create a #{self.class::RSRC_OBJECT_KEY}." unless args[:name]

      raise JSS::AlreadyExistsError, "A #{self.class::RSRC_OBJECT_KEY} already exists with the name '#{args[:name]}'" if self.class.all_names(api: @api).include? args[:name]
    end