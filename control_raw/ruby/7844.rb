def add_face_from_stream(large_person_group_id, person_id, image, user_data:nil, target_face:nil, custom_headers:nil)
      response = add_face_from_stream_async(large_person_group_id, person_id, image, user_data:user_data, target_face:target_face, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end