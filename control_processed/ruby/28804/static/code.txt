def contents
      c = StringIO.new
      @lines.each do |l| 
        c.puts l if l
      end
      c.string
    end