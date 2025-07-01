def parse_comments
      stack = []
      matched = parse_comment
      while matched != :failed
        stack << matched
        matched = parse_comment
      end
      stack
    end