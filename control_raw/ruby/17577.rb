def parse(node)
      node.attributes.each do |key, value|
        case key
        when 'type'
          @type = value.value.to_sym
        when 'styleId'
          @style_id = value.value
        when 'default'
          @default = attribute_enabled?(value.value)
        end
      end
      node.xpath('*').each do |subnode|
        case subnode.name
        when 'name'
          @name = subnode.attribute('val').value
        when 'basedOn'
          @based_on = subnode.attribute('val').value
        when 'next'
          @next_style = subnode.attribute('val').value
        when 'rPr'
          @run_properties = DocxParagraphRun.new(parent: self).parse_properties(subnode)
        when 'pPr'
          @paragraph_properties = ParagraphProperties.new(parent: self).parse(subnode)
        when 'tblPr'
          @table_properties = TableProperties.new(parent: self).parse(subnode)
        when 'trPr'
          @table_row_properties = TableRowProperties.new(parent: self).parse(subnode)
        when 'tcPr'
          @table_cell_properties = CellProperties.new(parent: self).parse(subnode)
        when 'tblStylePr'
          @table_style_properties_list << TableStyleProperties.new(parent: self).parse(subnode)
        when 'qFormat'
          @q_format = true
        end
      end
      fill_empty_table_styles
      self
    end