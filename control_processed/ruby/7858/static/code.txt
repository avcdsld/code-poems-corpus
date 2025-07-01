def delete_at_management_group(policy_set_definition_name, management_group_id, custom_headers:nil)
      response = delete_at_management_group_async(policy_set_definition_name, management_group_id, custom_headers:custom_headers).value!
      nil
    end