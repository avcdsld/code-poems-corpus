def rest_xml
      doc = REXML::Document.new APIConnection::XML_HEADER
      ns = doc.add_element 'network_segment'
      ns.add_element('building').text = @building
      ns.add_element('department').text = @department
      ns.add_element('distribution_point').text = @distribution_point
      ns.add_element('ending_address').text = @ending_address.to_s
      ns.add_element('name').text = @name
      ns.add_element('netboot_server').text = @netboot_server
      ns.add_element('override_buildings').text = @override_buildings
      ns.add_element('override_departments').text = @override_departments
      ns.add_element('starting_address').text = @starting_address.to_s
      ns.add_element('swu_server').text = @swu_server
      doc.to_s
    end