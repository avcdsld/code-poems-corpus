def map &block
      if empty? then
        None.new
      else
        Some.new(block.call(get))
      end
    end