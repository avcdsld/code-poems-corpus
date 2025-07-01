def parse(node)
      node.attributes.each do |key, value|
        case key
        when 'showButton'
          @show_button = attribute_enabled?(value)
        end
      end

      node.xpath('*').each do |node_child|
        case node_child.name
        when 'customFilters'
          @custom_filters = CustomFilters.new(parent: self).parse(node_child)
        end
      end
      self
    end