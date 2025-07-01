def save(connection, comment = nil)
      validate

      xml = connection.make_xml('VulnerabilityExceptionCreateRequest')
      xml.add_attributes({ 'vuln-id' => @vuln_id,
                           'scope' => @scope,
                           'reason' => @reason })
      case @scope
      when Scope::ALL_INSTANCES_ON_A_SPECIFIC_ASSET
        xml.add_attributes({ 'device-id' => @asset_id })
      when Scope::SPECIFIC_INSTANCE_OF_SPECIFIC_ASSET
        xml.add_attributes({ 'device-id' => @asset_id,
                             'port-no' => @port,
                             'vuln-key' => @vuln_key })
      when Scope::ALL_INSTANCES_IN_A_SPECIFIC_SITE
        xml.add_attributes({ 'site-id ' => @site_id })
      end

      @submitter_comment = comment if comment
      if @submitter_comment
        comment_elem = REXML::Element.new('comment')
        comment_elem.add_text(@submitter_comment)
        xml.add_element(comment_elem)
      end

      response = connection.execute(xml, '1.2')
      @id = response.attributes['exception-id'].to_i if response.success
    end