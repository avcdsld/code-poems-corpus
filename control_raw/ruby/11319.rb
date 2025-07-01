def ocrmethod_with_http_info(language, cache_image:nil, enhanced:false, custom_headers:nil)
      ocrmethod_async(language, cache_image:cache_image, enhanced:enhanced, custom_headers:custom_headers).value!
    end