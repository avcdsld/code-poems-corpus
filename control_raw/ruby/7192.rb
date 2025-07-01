def cancel(job_name, custom_headers:nil)
      response = cancel_async(job_name, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end