def push *elements
      elements.each do |element|
        node = LLNode.new(element, nil, @last)
        @first = node if @first.nil?
        @last.next = node unless @last.nil?
        @last = node
        @size += 1
      end
      self
    end