def parse(node)
      node.xpath('*').each do |node_child|
        case node_child.name
        when 'tableStyleId'
          @table_style_id = node_child.text
        when 'tblBorders'
          @table_borders = TableBorders.new(parent: self).parse(node_child)
        when 'tblStyle'
          # TODO: Incorrect but to keep compatibility
          @table_style_element = TableStyle.new(parent: self).parse(node_child)
        when 'tblW'
          @table_width = OoxmlSize.new.parse(node_child)
        when 'jc'
          @jc = node_child.attribute('val').text.to_sym
        when 'shd'
          @shade = Shade.new(parent: self).parse(node_child)
        when 'solidFill'
          @fill = PresentationFill.new(parent: self).parse(node)
        when 'tblLook'
          @table_look = TableLook.new(parent: self).parse(node_child)
        when 'tblInd'
          @table_indent = OoxmlSize.new(node_child.attribute('w').text.to_f)
        when 'tblpPr'
          @table_positon = TablePosition.new(parent: self).parse(node_child)
        when 'tblCellMar'
          @table_cell_margin = TableMargins.new(parent: table_properties).parse(node_child)
        when 'tblStyleColBandSize'
          @table_style_column_band_size = TableStyleColumnBandSize.new(parent: self).parse(node_child)
        when 'tblStyleRowBandSize'
          @table_style_row_band_size = TableStyleRowBandSize.new(parent: self).parse(node_child)
        when 'tblLayout'
          @table_layout = TableLayout.new(parent: self).parse(node_child)
        when 'tblCellSpacing'
          @table_cell_spacing = OoxmlSize.new.parse(node_child)
        when 'tblCaption'
          @caption = ValuedChild.new(:string, parent: self).parse(node_child)
        when 'tblDescription'
          @description = ValuedChild.new(:string, parent: self).parse(node_child)
        end
      end
      @table_look = TableLook.new(parent: self).parse(node) if @table_look.nil?
      self
    end