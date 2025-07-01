def list_hierarchical_entities_with_http_info(app_id, version_id, skip:0, take:100, custom_headers:nil)
      list_hierarchical_entities_async(app_id, version_id, skip:skip, take:take, custom_headers:custom_headers).value!
    end