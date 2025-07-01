def create_or_update(resource_group_name, load_balancer_name, inbound_nat_rule_name, inbound_nat_rule_parameters, custom_headers:nil)
      response = create_or_update_async(resource_group_name, load_balancer_name, inbound_nat_rule_name, inbound_nat_rule_parameters, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end