def aces_level=(level)
      return if level.nil?
      return unless ['full', 'default', 'none'].include? level.downcase
      logging = REXML::XPath.first(@xml, 'ScanTemplate/Logging')
      if logging.nil?
        logging = REXML::Element.new('Logging')
        @xml.add_element(logging)
      end
      aces = REXML::XPath.first(logging, 'aces')
      if aces.nil?
        aces = REXML::Element.new('aces')
        logging.add_element(aces)
      end
      aces.attributes['level'] = level
    end