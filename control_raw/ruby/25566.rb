def parse_xy
      s0 = @current_pos
      s1 = match_digit
      if s1 != :failed
        s2 = match_digit
        if s2 != :failed
          @reported_pos = s0
          s0 = { "x" => s1.to_i, "y" => s2.to_i }
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