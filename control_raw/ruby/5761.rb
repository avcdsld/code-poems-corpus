def configured_name_key(name)
      is_property_tag = MetaTags.config.property_tags.any? do |tag_name|
        name.to_s.match(/^#{Regexp.escape(tag_name.to_s)}\b/)
      end
      is_property_tag ? :property : :name
    end