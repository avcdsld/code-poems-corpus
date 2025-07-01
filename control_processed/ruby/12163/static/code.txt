def pos *indexes
      positions = indexes.map do |index|
        if include? index
          @cat_hash[index]
        elsif index.is_a?(Numeric) && index < @array.size
          index
        else
          raise IndexError, "#{index.inspect} is neither a valid category"\
            ' nor a valid position'
        end
      end

      positions.flatten!
      positions.size == 1 ? positions.first : positions.sort
    end