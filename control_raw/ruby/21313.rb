def wait_for_answer(opts = {})
      receive_trying opts
      receive_ringing opts
      receive_progress opts
      receive_answer opts
      ack_answer opts
    end