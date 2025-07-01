def delete_synonym!(objectID, forward_to_replicas = false, request_options = {})
      res = delete_synonym(objectID, forward_to_replicas, request_options)
      wait_task(res['taskID'], WAIT_TASK_DEFAULT_TIME_BEFORE_RETRY, request_options)
      res
    end