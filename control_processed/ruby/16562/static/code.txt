def index( child )
      count = -1
      @children.find { |i| count += 1 ; i.hash == child.hash }
      count
    end