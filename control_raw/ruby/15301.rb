def delete!(request_options = {})
      res = delete(request_options)
      wait_task(res['taskID'], WAIT_TASK_DEFAULT_TIME_BEFORE_RETRY, request_options)
      res
    end