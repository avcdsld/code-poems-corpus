def content_match?(content)
      if pattern.is_a?(String)
        content.any? { |thing| thing == pattern }
      else
        content.any? { |thing| thing =~ pattern }
      end
    end