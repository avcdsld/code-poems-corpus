def pluralize(word)
      result = word.to_s.dup

      if word.empty? || inflections.uncountables.include?(result.downcase)
        result
      else
        inflections.plurals.each { |(rule, replacement)| break if result.gsub!(rule, replacement) }
        result
      end
    end