def recognize_text(url, detect_handwriting:false, custom_headers:nil)
      response = recognize_text_async(url, detect_handwriting:detect_handwriting, custom_headers:custom_headers).value!
      nil
    end