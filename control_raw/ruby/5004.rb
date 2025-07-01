def class_operation_module
      @class_operation_module ||= Module.new {

        def client(globals = {})
          @client ||= Savon::Client.new(globals)
        rescue InitializationError
          raise_initialization_error!
        end

        def global(option, *value)
          client.globals[option] = value
        end

        def raise_initialization_error!
          raise InitializationError,
            "Expected the model to be initialized with either a WSDL document or the SOAP endpoint and target namespace options.\n" \
            "Make sure to setup the model by calling the .client class method before calling the .global method.\n\n" \
            "client(wsdl: '/Users/me/project/service.wsdl')                              # to use a local WSDL document\n" \
            "client(wsdl: 'http://example.com?wsdl')                                     # to use a remote WSDL document\n" \
            "client(endpoint: 'http://example.com', namespace: 'http://v1.example.com')  # if you don't have a WSDL document"
        end

      }.tap { |mod| extend(mod) }
    end