def parse_split
      s0 = @current_pos
      s1 = match_str("手数----指手--")
      if s1 != :failed
        s2 = match_str("-------消費時間--")
        s2 = nil if s2 == :failed
        s3 = parse_nl
        if s3 != :failed
          s0 = [s1, s2, s3]
        else
          @current_pos = s0
          s0 = :failed
        end
      else
        @current_pos = s0
        s0 = :failed
      end
      s0
    end