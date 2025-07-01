def delete_sub_list_with_http_info(app_id, version_id, cl_entity_id, sub_list_id, custom_headers:nil)
      delete_sub_list_async(app_id, version_id, cl_entity_id, sub_list_id, custom_headers:custom_headers).value!
    end