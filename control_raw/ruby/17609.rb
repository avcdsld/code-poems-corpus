def parse
      OOXMLDocumentObject.add_to_xmls_stack(@xml_path)
      @name = File.basename(@xml_path, '.*')
      node = parse_xml(OOXMLDocumentObject.current_xml)
      node.xpath('//p:sld/*').each do |node_child|
        case node_child.name
        when 'cSld'
          @common_slide_data = CommonSlideData.new(parent: self).parse(node_child)
        when 'timing'
          @timing = Timing.new(parent: self).parse(node_child)
        when 'transition'
          @transition = Transition.new(parent: self).parse(node_child)
        when 'AlternateContent'
          @alternate_content = PresentationAlternateContent.new(parent: self).parse(node_child)
        end
      end
      OOXMLDocumentObject.xmls_stack.pop
      @relationships = Relationships.new(parent: self).parse_file("#{OOXMLDocumentObject.path_to_folder}#{File.dirname(@xml_path)}/_rels/#{@name}.xml.rels")
      parse_note
      self
    end