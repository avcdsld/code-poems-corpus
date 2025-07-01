def enabled_vuln_checks
      checks = REXML::XPath.first(@xml, '//VulnerabilityChecks/Enabled')
      checks ? checks.elements.to_a('Check').map { |c| c.attributes['id'] } : []
    end