def get_partition_health(partition_id, events_health_state_filter:0, replicas_health_state_filter:0, exclude_health_statistics:false, timeout:60, custom_headers:nil)
      response = get_partition_health_async(partition_id, events_health_state_filter:events_health_state_filter, replicas_health_state_filter:replicas_health_state_filter, exclude_health_statistics:exclude_health_statistics, timeout:timeout, custom_headers:custom_headers).value!
      response.body unless response.nil?
    end