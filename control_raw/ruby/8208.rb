def cancel_at_resource(resource_id, remediation_name, custom_headers:nil)
      response = cancel_at_resource_async(resource_id, remediation_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end