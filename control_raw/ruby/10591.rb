def model_status_with_http_info(resource_group_name, hub_name, prediction_name, parameters, custom_headers:nil)
      model_status_async(resource_group_name, hub_name, prediction_name, parameters, custom_headers:custom_headers).value!
    end