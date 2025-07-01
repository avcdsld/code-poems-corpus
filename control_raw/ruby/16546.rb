def lock(path, body, initheader = nil)
      request(Lock.new(path, initheader), body)
    end