def scan_devices_with_schedule(devices, schedules)
      site_id = devices.map(&:site_id).uniq.first
      xml     = make_xml('SiteDevicesScanRequest', 'site-id' => site_id)
      elem    = REXML::Element.new('Devices')
      devices.each do |device|
        elem.add_element('device', 'id' => "#{device.id}")
      end
      xml.add_element(elem)
      scheds = REXML::Element.new('Schedules')
      schedules.each { |sched| scheds.add_element(sched.as_xml) }
      xml.add_element(scheds)

      _scan_ad_hoc_with_schedules(xml)
    end