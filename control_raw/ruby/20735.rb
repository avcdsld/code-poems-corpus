def add_underscore_to(file)
      f = Pathname.new(file)
      if f.basename.to_s =~ /^_/
        file
      else
        "#{f.dirname}/_#{f.basename}"
      end
    end