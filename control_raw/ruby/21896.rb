def ingress_interface
      list = config_get('itd_service', 'ingress_interface', @get_args)
      rlist = []
      list.each do |intf, next_hop|
        intf.gsub!('Eth', 'ethernet ')
        intf.gsub!('Po', 'port-channel ')
        intf.gsub!('Vlan', 'vlan ')
        next_hop = '' if next_hop.nil?
        rlist << [intf, next_hop]
      end
      rlist
    end