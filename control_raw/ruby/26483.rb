def find(name)
      request = Message::Find.new(Thread.mailbox, name)
      methods = send_request request
      return nil if methods.is_a? NilClass
      rsocket # open relay pipe to avoid race conditions
      actor = DCell::ActorProxy.create.new self, name, methods
      add_actor actor
    end