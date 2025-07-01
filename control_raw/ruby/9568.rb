def list_query_results_for_policy_definition(policy_states_resource, subscription_id, policy_definition_name, query_options:nil, custom_headers:nil)
      response = list_query_results_for_policy_definition_async(policy_states_resource, subscription_id, policy_definition_name, query_options:query_options, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end