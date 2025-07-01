def parse_comment
      s0 = @current_pos
      if match_str("'") != :failed
        s2 = parse_nonls
        if parse_nl != :failed
          @reported_pos = s0
          s2.join
        else
          @current_pos = s0
          :failed
        end
      else
        @current_pos = s0
        :failed
      end
    end