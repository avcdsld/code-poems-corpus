def list_swagger(resource_group_name, workflow_name, custom_headers:nil)
      response = list_swagger_async(resource_group_name, workflow_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end