def begin_unplanned_failover(fabric_name, protection_container_name, replicated_protected_item_name, failover_input, custom_headers:nil)
      response = begin_unplanned_failover_async(fabric_name, protection_container_name, replicated_protected_item_name, failover_input, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end