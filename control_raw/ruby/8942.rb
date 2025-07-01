def create_pattern_any_entity_model_with_http_info(app_id, version_id, extractor_create_object, custom_headers:nil)
      create_pattern_any_entity_model_async(app_id, version_id, extractor_create_object, custom_headers:custom_headers).value!
    end