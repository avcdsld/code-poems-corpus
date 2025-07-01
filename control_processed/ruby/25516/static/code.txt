def parse_place
      s0 = @current_pos
      s1 = parse_num
      if s1 != :failed
        s2 = parse_numkan
        if s2 != :failed
          @reported_pos = s0
          s0 = { "x" => s1, "y" => s2 }
        else
          @current_pos = s0
          s0 = :failed
        end
      else
        @current_pos = s0
        s0 = :failed
      end
      if s0 == :failed
        s0 = @current_pos
        if match_regexp("同") != :failed
          match_str("　")
          @reported_pos = s0
          s0 = { "same" => true }
        else
          @current_pos = s0
          s0 = :failed
        end
      end
      s0
    end