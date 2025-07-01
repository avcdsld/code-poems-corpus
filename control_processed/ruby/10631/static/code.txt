def update_patterns(app_id, version_id, patterns, custom_headers:nil)
      response = update_patterns_async(app_id, version_id, patterns, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end