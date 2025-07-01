def list_prebuilt_entities(app_id, version_id, custom_headers:nil)
      response = list_prebuilt_entities_async(app_id, version_id, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end