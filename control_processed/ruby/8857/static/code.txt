def add_prebuilt(app_id, version_id, prebuilt_extractor_names, custom_headers:nil)
      response = add_prebuilt_async(app_id, version_id, prebuilt_extractor_names, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end