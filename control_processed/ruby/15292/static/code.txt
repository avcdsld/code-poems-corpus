def copy_rules!(src_index, dst_index, request_options = {})
      res = copy_rules(src_index, dst_index, request_options)
      wait_task(dst_index, res['taskID'], WAIT_TASK_DEFAULT_TIME_BEFORE_RETRY, request_options)
      res
    end