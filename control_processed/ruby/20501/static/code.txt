def append(event, method = nil, oneshot = false, &block)
      callback = Callback.new(self, event, method||block, oneshot)
      (@listeners[event] ||= []) << callback
      callback
    end