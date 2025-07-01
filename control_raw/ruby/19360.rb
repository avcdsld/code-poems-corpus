def as_xml
      xml = REXML::Element.new('AssetGroup')
      xml.attributes['id']          = @id
      xml.attributes['name']        = @name
      xml.attributes['description'] = @description

      if @description && !@description.empty?
        elem = REXML::Element.new('Description')
        elem.add_text(@description)
        xml.add_element(elem)
      end

      elem = REXML::Element.new('Devices')
      @assets.each { |a| elem.add_element('device', { 'id' => a.id }) }
      xml.add_element(elem)

      unless tags.empty?
        tag_xml = xml.add_element(REXML::Element.new('Tags'))
        @tags.each { |tag| tag_xml.add_element(tag.as_xml) }
      end

      xml
    end