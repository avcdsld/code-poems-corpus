def request_service(name)
      # Use RequestName, but asynchronously!
      # A synchronous call would not work with service activation, where
      # method calls to be serviced arrive before the reply for RequestName
      # (Ticket#29).
      proxy.RequestName(name, NAME_FLAG_REPLACE_EXISTING) do |rmsg, r|
        # check and report errors first
        raise rmsg if rmsg.is_a?(Error)
        raise NameRequestError unless r == REQUEST_NAME_REPLY_PRIMARY_OWNER
      end
      @service = Service.new(name, self)
      @service
    end