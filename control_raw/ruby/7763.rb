def begin_manage_deployments(resource_group_name, service_name, parameters, custom_headers:nil)
      response = begin_manage_deployments_async(resource_group_name, service_name, parameters, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end