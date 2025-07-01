def assert(truthy, label = nil, objects = nil)
      if (RMQ.app.development? || RMQ.app.test?) && !truthy
        label ||= 'Assert failed'
        if block_given? && !objects
          objects = yield
        end
        log_detailed label, objects: objects, skip_first_caller: true
      end
    end