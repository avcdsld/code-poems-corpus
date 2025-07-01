def process_update_job_from_file(file_path, report_email = nil, postback_url = nil, options = {})
      data = options
      data['file'] = file_path
      process_job(:update, data, report_email, postback_url, 'file')
    end