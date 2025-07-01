def get_schools_for_teacher(id, opts = {})
      data, _status_code, _headers = get_schools_for_teacher_with_http_info(id, opts)
      return data
    end