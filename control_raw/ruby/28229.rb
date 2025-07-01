def get_default_network(zone)
      params = {
          'command' => 'listNetworks',
          'isDefault' => true,
          'zoneid' => zone
      }
      json = send_request(params)

      networks = json['network']
      return nil if !networks || networks.empty?

      default = networks.first
      return default if networks.length == 1

      networks.each { |n|
        if n['type'] == 'Direct' then
          default = n
          break
        end
      }

      default
    end