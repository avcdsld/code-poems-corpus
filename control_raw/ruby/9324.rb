def disable(resource_group_name, job_collection_name, custom_headers:nil)
      response = disable_async(resource_group_name, job_collection_name, custom_headers:custom_headers).value!
      nil
    end