def to_xml(options = {})
      pcap_path = options[:pcap_path]
      docdup = doc.dup

      # Not removing in reverse would most likely remove the wrong
      # nodes because of changing indices.
      @media_nodes.reverse.each do |nop|
        nopdup = docdup.xpath(nop.path)

        if pcap_path.nil? or @media.blank?
          nopdup.remove
        else
          exec = nopdup.xpath("./action/exec").first
          exec['play_pcap_audio'] = pcap_path
        end
      end

      unless @reference_variables.empty?
        scenario_node = docdup.xpath('scenario').first
        scenario_node << docdup.create_element('Reference') do |ref|
          ref[:variables] = @reference_variables.to_a.join ','
        end
      end

      docdup.to_xml
    end