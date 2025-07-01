def update_pattern(app_id, version_id, pattern_id, pattern, custom_headers:nil)
      response = update_pattern_async(app_id, version_id, pattern_id, pattern, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end