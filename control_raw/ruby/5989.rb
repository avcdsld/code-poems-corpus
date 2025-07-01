def adjust_security_groups(options)
      return options unless options[:network_configuration] &&
                     options[:network_configuration][:awsvpc_configuration]

      awsvpc_conf = options[:network_configuration][:awsvpc_configuration]

      security_groups = awsvpc_conf[:security_groups]
      if [nil, '', 'nil'].include?(security_groups)
        security_groups = []
      end
      if security_groups.empty?
        fetch = Network::Fetch.new(network[:vpc])
        sg = fetch.security_group_id
        security_groups << sg
        security_groups.uniq!
      end

      # override security groups
      options[:network_configuration][:awsvpc_configuration][:security_groups] = security_groups
      options
    end