def split_version(full_name)
      matches = full_name.match(/(.*?)(?:[\.\-\_ ~,]?([0-9].*))?$/)
      if !matches.nil? && matches.length > 1
        [matches[1], matches[2]]
      else
        [full_string, nil]
      end
    end