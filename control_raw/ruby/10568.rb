def begin_update(resource_group_name, registry_name, build_task_name, step_name, build_step_update_parameters, custom_headers:nil)
      response = begin_update_async(resource_group_name, registry_name, build_task_name, step_name, build_step_update_parameters, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end