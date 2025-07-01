def flunk(workitem, error_class_or_instance_or_message, *err_arguments)

      err = error_class_or_instance_or_message
      trace = Ruote.pop_trace(err_arguments)

      err =
        case err
          when Exception
            err
          when Class
            err.new(*err_arguments)
          when String
            begin
              Ruote.constantize(err).new(*err_arguments)
            rescue #NameError # rescue instanciation errors too
              RuntimeError.new(err)
            end
          else
            ArgumentError.new(
              "flunk() failed, cannot bring back err from #{err.inspect}")
        end

      err.set_backtrace(trace || err.backtrace || caller)

      workitem = workitem.to_h if workitem.respond_to?(:to_h)

      at = Ruote.now_to_utc_s

      @context.storage.put_msg(
        'raise',
        'fei' => workitem['fei'],
        'wfid' => workitem['wfid'],
        'msg' => {
          'action' => 'dispatch',
          'fei' => workitem['fei'],
          'participant_name' => workitem['participant_name'],
          'participant' => nil,
          'workitem' => workitem,
          'put_at' => at
        },
        'error' => {
          'class' => err.class.name,
          'message' => err.message,
          'trace' => err.backtrace,
          'at' => at,
          'details' => err.respond_to?(:ruote_details) ? err.ruote_details : nil
        })
    end