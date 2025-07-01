def each(include_blank = false)
      @lines.each do |line|
        if include_blank || ! (line.is_a?(Array) ? line.empty? : line.blank?)
          yield(line)
        end
      end
    end