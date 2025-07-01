def delete(resource_group_name, ddos_protection_plan_name, custom_headers:nil)
      response = delete_async(resource_group_name, ddos_protection_plan_name, custom_headers:custom_headers).value!
      nil
    end