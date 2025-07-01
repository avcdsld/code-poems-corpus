def send_request(subject_name, client_id, request, options, &callback)
      request_id = generate_request_id
      request["reply_to"] = "#{@inbox_name}.#{client_id}.#{request_id}"
      @lock.synchronize do
        @requests[request_id] = [callback, options]
      end

      sanitized_log_message = sanitize_log_message(request)
      request_body = JSON.generate(request)

      @logger.debug("SENT: #{subject_name} #{sanitized_log_message}") unless options['logging'] == false

      EM.schedule do
        subscribe_inbox
        if @handled_response
          nats.publish(subject_name, request_body)
        else
          nats.flush do
            nats.publish(subject_name, request_body)
          end
        end
      end
      request_id
    end