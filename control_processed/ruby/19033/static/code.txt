def square_roots(n)
      raise ArgumentError, "Not a member of the field: #{n}." if !include?(n)
      case
      when prime == 2 then [n]
      when (prime % 4) == 3 then square_roots_for_p_3_mod_4(n)
      when (prime % 8) == 5 then square_roots_for_p_5_mod_8(n)
      else square_roots_default(n)
      end
    end