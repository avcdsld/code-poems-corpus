def parse(node, default_paragraph, default_character)
      node.xpath('*').each do |pg_size_subnode|
        case pg_size_subnode.name
        when 'pgSz'
          @size = PageSize.new.parse(pg_size_subnode)
        when 'pgBorders'
          page_borders = Borders.new
          page_borders.display = pg_size_subnode.attribute('display').value.to_sym unless pg_size_subnode.attribute('display').nil?
          page_borders.offset_from = pg_size_subnode.attribute('offsetFrom').value.to_sym unless pg_size_subnode.attribute('offsetFrom').nil?
          pg_size_subnode.xpath('w:bottom').each do |bottom|
            page_borders.bottom = BordersProperties.new(parent: page_borders).parse(bottom)
          end
          pg_size_subnode.xpath('w:left').each do |left|
            page_borders.bottom = BordersProperties.new(parent: page_borders).parse(left)
          end
          pg_size_subnode.xpath('w:top').each do |top|
            page_borders.bottom = BordersProperties.new(parent: page_borders).parse(top)
          end
          pg_size_subnode.xpath('w:right').each do |right|
            page_borders.bottom = BordersProperties.new(parent: page_borders).parse(right)
          end
          @page_borders = page_borders
        when 'type'
          @type = pg_size_subnode.attribute('val').value
        when 'pgMar'
          @margins = PageMargins.new(parent: self).parse(pg_size_subnode)
        when 'pgNumType'
          @num_type = pg_size_subnode.attribute('fmt').value unless pg_size_subnode.attribute('fmt').nil?
        when 'formProt'
          @form_prot = pg_size_subnode.attribute('val').value
        when 'textDirection'
          @text_direction = pg_size_subnode.attribute('val').value
        when 'docGrid'
          @document_grid = DocumentGrid.new(parent: self).parse(pg_size_subnode)
        when 'titlePg'
          @title_page = option_enabled?(pg_size_subnode)
        when 'cols'
          @columns = Columns.new.parse(pg_size_subnode)
        when 'headerReference', 'footerReference'
          target = OOXMLDocumentObject.get_link_from_rels(pg_size_subnode.attribute('id').value)
          OOXMLDocumentObject.add_to_xmls_stack("word/#{target}")
          note = Note.parse(default_paragraph: default_paragraph,
                            default_character: default_character,
                            target: target,
                            assigned_to: pg_size_subnode.attribute('type').value,
                            type: File.basename(target).sub('.xml', ''),
                            parent: self)
          @notes << note
          OOXMLDocumentObject.xmls_stack.pop
        when 'footnotePr'
          @footnote_properties = FootnoteProperties.new(parent: self).parse(pg_size_subnode)
        end
      end
      self
    end