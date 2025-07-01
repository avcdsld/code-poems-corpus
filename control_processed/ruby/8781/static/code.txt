def update_iteration(project_id, iteration_id, updated_iteration, custom_headers:nil)
      response = update_iteration_async(project_id, iteration_id, updated_iteration, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end