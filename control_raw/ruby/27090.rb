def request(method, *options)
      response_handler = if options.last.is_a?(Hash) && options.last[:handler]
                           options.last.delete(:handler)
                         else
                           handler
                         end

      self.class.base_uri Jiralicious.uri
      before_request if respond_to?(:before_request)
      response = self.class.send(method, *options)
      after_request(response) if respond_to?(:after_request)

      response_handler.call(response)
    end