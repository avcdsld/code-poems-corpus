def get_replica_info_with_http_info(partition_id, replica_id, timeout:60, custom_headers:nil)
      get_replica_info_async(partition_id, replica_id, timeout:timeout, custom_headers:custom_headers).value!
    end