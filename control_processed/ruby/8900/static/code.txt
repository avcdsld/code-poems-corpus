def delete_prebuilt(app_id, version_id, prebuilt_id, custom_headers:nil)
      response = delete_prebuilt_async(app_id, version_id, prebuilt_id, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end