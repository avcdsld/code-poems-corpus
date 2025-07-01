def generate_tag(suffix=nil)
      n = DateTime.now
      y, m = n.year.to_s.rjust(4, "20"), n.month.to_s.rjust(2, "0")
      d, u = n.mday.to_s.rjust(2, "0"), Rudy.sysinfo.user
      criteria = [y, m, d, u]
      criteria << suffix unless suffix.nil? || suffix.empty?
      criteria.join Rudy::DELIM 
    end