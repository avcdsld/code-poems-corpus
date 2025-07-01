def select(from: nil, to: nil, &block)
      retval = []

      each_with_depth(from: from, to: to) do |line, depth, index|
        retval << line if (block_given? == false || block.call(line, depth, index))
      end

      retval
    end