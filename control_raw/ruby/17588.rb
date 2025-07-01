def parse(node)
      case node.name
      when 'moveTo'
        @type = :move
      when 'lnTo'
        @type = :line
      when 'arcTo'
        @type = :arc
      when 'cubicBezTo'
        @type = :cubic_bezier
      when 'quadBezTo'
        @type = :quadratic_bezier
      when 'close'
        @type = :close
      end

      node.xpath('*').each do |node_child|
        case node_child.name
        when 'pt'
          @points << OOXMLCoordinates.parse(node_child)
        end
      end
      self
    end