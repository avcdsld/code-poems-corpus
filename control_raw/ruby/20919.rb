def push_content(title, url, date = nil, tags = nil, vars = {}, options = {})
      data = options
      data[:title] = title
      data[:url] = url
      if date != nil
        data[:date] = date
      end
      if tags != nil
        if tags.class == Array
          tags = tags.join(',')
        end
        data[:tags] = tags
      end
      if vars.length > 0
        data[:vars] = vars
      end
      api_post(:content, data)
    end