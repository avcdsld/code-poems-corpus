def networks=(should_list)
      delta_hash = Utils.delta_add_remove(should_list, networks)
      return if delta_hash.values.flatten.empty?
      [:add, :remove].each do |action|
        Cisco::Logger.debug("networks delta #{@get_args}\n #{action}: " \
                            "#{delta_hash[action]}")
        delta_hash[action].each do |network, route_map_policy|
          state = (action == :add) ? '' : 'no'
          network = Utils.process_network_mask(network)
          unless route_map_policy.nil?
            route_map = "route-map #{route_map_policy}"
            route_policy = "route-policy #{route_map_policy}"
          end
          set_args_keys(state: state, network: network, route_map: route_map,
                        route_policy: route_policy)
          config_set('bgp_af', 'networks', @set_args)
        end
      end
    end