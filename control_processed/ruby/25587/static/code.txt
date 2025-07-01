def listen_queues(*queues, &block)
      queues = determine_queue_names(queues)
      subscriber.listen_queues(queues, &block)
    end