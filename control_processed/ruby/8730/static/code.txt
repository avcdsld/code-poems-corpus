def detect_with_stream(image, return_face_id:true, return_face_landmarks:false, return_face_attributes:nil, recognition_model:nil, return_recognition_model:false, custom_headers:nil)
      response = detect_with_stream_async(image, return_face_id:return_face_id, return_face_landmarks:return_face_landmarks, return_face_attributes:return_face_attributes, recognition_model:recognition_model, return_recognition_model:return_recognition_model, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end