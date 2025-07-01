def disable_vuln_check(check_id)
      checks = REXML::XPath.first(@xml, '//VulnerabilityChecks')
      checks.elements.delete("Enabled/Check[@id='#{check_id}']")
      disabled_checks = checks.elements['Disabled'] || checks.add_element('Disabled')
      disabled_checks.add_element('Check', { 'id' => check_id })
    end