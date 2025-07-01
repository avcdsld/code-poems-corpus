def add element=nil
      rv = nil
      if element.nil?
        Element.new("", self, @element.context)
      elsif not element.kind_of?(Element)
        Element.new(element, self, @element.context)
      else
        @element << element
        element.context = @element.context
        element
      end
    end