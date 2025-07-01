def parse_fugou
      s0 = @current_pos
      s1 = parse_place
      if s1 != :failed
        s2 = parse_piece
        if s2 != :failed
          s3 = match_str("成")
          s3 = nil if s3 == :failed
          @reported_pos = s0
          s0 = { "to" => s1, "piece" => s2, "promote" => !!s3 }
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