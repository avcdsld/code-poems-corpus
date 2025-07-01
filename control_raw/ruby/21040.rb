def effective_properties(category_name, event_name, additional_properties = { })
      event = version_object.fetch_event(category_name, event_name)

      explicit = { }
      self.class.merge_properties(explicit, additional_properties, property_separator)
      properties = @implicit_properties.merge(explicit)

      event.validate!(properties)
      # We need to do this instead of just using || so that you can override a present distinct_id with nil.
      net_distinct_id = if properties.has_key?('distinct_id') then properties.delete('distinct_id') else self.distinct_id end

      event_external_name = event.external_name || external_name.call(event)
      raise TypeError, "The external name of an event must be a String" unless event_external_name.kind_of?(String)

      {
        :distinct_id   => net_distinct_id,
        :event_name    => event.full_name,
        :external_name => event_external_name,
        :properties    => properties
      }
    end