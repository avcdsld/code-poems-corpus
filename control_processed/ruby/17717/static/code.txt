def parse(node)
      node.attributes.each do |key, value|
        case key
        when 'type'
          @type = value_to_symbol(value)
        when 'displayEmptyCellsAs'
          @display_empty_cells_as = value_to_symbol(value)
        when 'displayHidden'
          @display_hidden = attribute_enabled?(value)
        when 'displayXAxis'
          @display_x_axis = attribute_enabled?(value)
        when 'rightToLeft'
          @right_to_left = attribute_enabled?(value)
        when 'minAxisType'
          @min_axis_type = value_to_symbol(value)
        when 'maxAxisType'
          @max_axis_type = value_to_symbol(value)
        when 'manualMin'
          @manual_min = value.value.to_f
        when 'manualMax'
          @manual_max = value.value.to_f
        when 'lineWeight'
          @line_weight = OoxmlSize.new(value.value.to_f, :point)
        when 'high'
          @high_point = attribute_enabled?(value)
        when 'low'
          @low_point = attribute_enabled?(value)
        when 'first'
          @first_point = attribute_enabled?(value)
        when 'last'
          @last_point = attribute_enabled?(value)
        when 'negative'
          @negative_point = attribute_enabled?(value)
        when 'markers'
          @markers = attribute_enabled?(value)
        end
      end

      node.xpath('*').each do |node_child|
        case node_child.name
        when 'colorSeries'
          @color_series = OoxmlColor.new(parent: self).parse(node_child)
        when 'colorHigh'
          @color_high = OoxmlColor.new(parent: self).parse(node_child)
        when 'colorLow'
          @color_low = OoxmlColor.new(parent: self).parse(node_child)
        when 'colorFirst'
          @color_first = OoxmlColor.new(parent: self).parse(node_child)
        when 'colorLast'
          @color_last = OoxmlColor.new(parent: self).parse(node_child)
        when 'colorNegative'
          @color_negative = OoxmlColor.new(parent: self).parse(node_child)
        when 'colorMarkers'
          @color_markers = OoxmlColor.new(parent: self).parse(node_child)
        end
      end
      self
    end