def list_worker_pool_instance_metrics_next(next_page_link, custom_headers:nil)
      response = list_worker_pool_instance_metrics_next_async(next_page_link, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end