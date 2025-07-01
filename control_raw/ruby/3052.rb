def call(env)
      info      = (env[ENV_INFO_KEY] ||= RequestDetails.new)
      info.id ||= env[HTTP_X_REQUEST_ID] || env[ACTION_DISPATCH_REQUEST_ID] || SecureRandom.uuid

      time_started_service = Time.now                      # The wall time the request started being processed by rack
      ts_started_service   = fsecs                         # The monotonic time the request started being processed by rack
      time_started_wait    = RT._read_x_request_start(env) # The time the request was initially received by the web server (if available)
      effective_overtime   = (wait_overtime && RT._request_has_body?(env)) ? wait_overtime : 0 # additional wait timeout (if set and applicable)
      seconds_service_left = nil

      # if X-Request-Start is present and wait_timeout is set, expire requests older than wait_timeout (+wait_overtime when applicable)
      if time_started_wait && wait_timeout
        seconds_waited          = time_started_service - time_started_wait # how long it took between the web server first receiving the request and rack being able to handle it
        seconds_waited          = 0 if seconds_waited < 0                  # make up for potential time drift between the routing server and the application server
        final_wait_timeout      = wait_timeout + effective_overtime        # how long the request will be allowed to have waited
        seconds_service_left    = final_wait_timeout - seconds_waited      # first calculation of service timeout (relevant if request doesn't get expired, may be overriden later)
        info.wait, info.timeout = seconds_waited, final_wait_timeout       # updating the info properties; info.timeout will be the wait timeout at this point
        if seconds_service_left <= 0 # expire requests that have waited for too long in the queue (as they are assumed to have been dropped by the web server / routing layer at this point)
          RT._set_state! env, :expired
          raise RequestExpiryError.new(env), "Request older than #{info.ms(:timeout)}."
        end
      end

      # pass request through if service_timeout is false (i.e., don't time it out at all.)
      return @app.call(env) unless service_timeout

      # compute actual timeout to be used for this request; if service_past_wait is true, this is just service_timeout. If false (the default), and wait time was determined, we'll use the shortest value between seconds_service_left and service_timeout. See comment above at service_past_wait for justification.
      info.timeout = service_timeout # nice and simple, when service_past_wait is true, not so much otherwise:
      info.timeout = seconds_service_left if !service_past_wait && seconds_service_left && seconds_service_left > 0 && seconds_service_left < service_timeout

      RT._set_state! env, :ready                            # we're good to go, but have done nothing yet

      heartbeat_event = nil                                 # init var so it's in scope for following proc
      register_state_change = ->(status = :active) {        # updates service time and state; will run every second
        heartbeat_event.cancel! if status != :active        # if the request is no longer active we should stop updating every second
        info.service = fsecs - ts_started_service           # update service time
        RT._set_state! env, status                          # update status
      }
      heartbeat_event = RT::Scheduler.run_every(1) { register_state_change.call :active }  # start updating every second while active; if log level is debug, this will log every sec

      timeout = RT::Scheduler::Timeout.new do |app_thread|  # creates a timeout instance responsible for timing out the request. the given block runs if timed out
        register_state_change.call :timed_out
        app_thread.raise(RequestTimeoutException.new(env), "Request #{"waited #{info.ms(:wait)}, then " if info.wait}ran for longer than #{info.ms(:timeout)}")
      end

      response = timeout.timeout(info.timeout) do           # perform request with timeout
        begin  @app.call(env)                               # boom, send request down the middleware chain
        rescue RequestTimeoutException => e                 # will actually hardly ever get to this point because frameworks tend to catch this. see README for more
          raise RequestTimeoutError.new(env), e.message, e.backtrace  # but in case it does get here, re-raise RequestTimeoutException as RequestTimeoutError
        ensure
          register_state_change.call :completed
        end
      end

      response
    end