def process_response_queue_message(metadata, payload)
      response_queue = @transactions.delete metadata.correlation_id
      response_queue << payload if response_queue
    end