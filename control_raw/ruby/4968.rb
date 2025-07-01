def contacts(opts={})
      # NOTE: caching functionality can be dependant of the nature of the list, if dynamic or not ...
      bypass_cache = opts.delete(:bypass_cache) { false }
      recent = opts.delete(:recent) { false }
      paged = opts.delete(:paged) { false }

      if bypass_cache || @contacts.nil?
        path = recent ? RECENT_CONTACTS_PATH : CONTACTS_PATH
        opts[:list_id] = @id

        response = Hubspot::Connection.get_json(path, Hubspot::ContactProperties.add_default_parameters(opts))
        @contacts = response['contacts'].map! { |c| Hubspot::Contact.from_result(c) }
        paged ? response : @contacts
      else
        @contacts
      end
    end