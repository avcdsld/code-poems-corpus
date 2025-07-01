def update_closed_list(app_id, version_id, cl_entity_id, closed_list_model_update_object, custom_headers:nil)
      response = update_closed_list_async(app_id, version_id, cl_entity_id, closed_list_model_update_object, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end