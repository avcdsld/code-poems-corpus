def postprocess
      @position &&= @position.to_s.rjust(2, '0')
      @year = @created.year
      @month = @created.month.to_s.rjust(2, '0')
      @day = @created.mday.to_s.rjust(2, '0')
      @hour = @created.hour.to_s.rjust(2, '0')
      @minute = @created.min.to_s.rjust(2, '0')
      @second = @created.sec.to_s.rjust(2, '0')
    end