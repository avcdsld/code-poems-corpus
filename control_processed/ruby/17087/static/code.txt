def docomo_guid_link_to(str, options = {})
      url = options
      if options.is_a?(Hash)
        options = options.symbolize_keys
        options[:guid] = 'ON'
        url = url_for(options)
      end
      link_to_url(str, url)
    end