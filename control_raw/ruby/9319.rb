def create_or_update_with_http_info(resource_group_name, job_collection_name, job_collection, custom_headers:nil)
      create_or_update_async(resource_group_name, job_collection_name, job_collection, custom_headers:custom_headers).value!
    end