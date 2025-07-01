def parse(node)
      node.xpath('*').each do |node_child|
        case node_child.name
        when 'idx'
          @index = ValuedChild.new(:integer, parent: self).parse(node_child)
        when 'order'
          @order = ValuedChild.new(:integer, parent: self).parse(node_child)
        when 'tx'
          @text = SeriesText.new(parent: self).parse(node_child)
        when 'cat'
          @categories = Categories.new(parent: self).parse(node_child)
        when 'dLbls'
          @display_labels = DisplayLabelsProperties.new(parent: self).parse(node_child)
        when 'val'
          @values = XYValues.new(parent: self).parse(node_child)
        when 'xVal'
          @x_values = XYValues.new(parent: self).parse(node_child)
        when 'yVal'
          @y_values = XYValues.new(parent: self).parse(node_child)
        end
      end
      self
    end