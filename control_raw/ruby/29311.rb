def safe_eval(str, **vars)
      return str if str.is_a?(Integer)

      # dentaku 2 doesn't support hex
      str = str.gsub(/0x[0-9a-zA-Z]+/) { |c| c.to_i(16) }
      Dentaku::Calculator.new.store(vars).evaluate(str)
    end