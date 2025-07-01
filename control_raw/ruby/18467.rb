def truncate(string, width, options={})
      trailing = options[:trailing] || '…'

      chars = string.to_s.chars.to_a
      if chars.length < width && chars.length > 3
        chars.join
      elsif chars.length > 3
        (chars[0, width - trailing.length].join) + trailing
      end
    end