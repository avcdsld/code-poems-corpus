def update_pattern_any_entity_role(app_id, version_id, entity_id, role_id, entity_role_update_object, custom_headers:nil)
      response = update_pattern_any_entity_role_async(app_id, version_id, entity_id, role_id, entity_role_update_object, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end