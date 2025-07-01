def netmask6(scope = :global)
      if [:global, :link].include?(scope)
        @network_conf["mask6_#{scope}".to_sym] ||= IPAddr.new('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff').mask(prefix6(scope)).to_s if prefix6(scope)
      else
        raise ArgumentError, "Unrecognized address scope #{scope}"
      end
    end